# 题目：778.水位上升的泳池中游泳
# 难度：HARD
# 最后提交：2022-09-19 11:53:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(t, x, y, v):
            if x == y == n-1:
                return True
            v.add((x, y))
            for nx, ny in [[x+1, y], [x-1, y], [x, y-1], [x, y+1]]:
                if 0 <=nx<n and 0<=ny<n and (nx, ny) not in v and grid[nx][ny]<=t:     
                    if dfs(t, nx, ny, v):
                        return True
            return False

        l = max(grid[0][0], grid[-1][-1])
        r = n * n - 1
        while l <= r:
            mid = l+r>>1
            if dfs(mid, 0, 0, set()):
                r = mid - 1
            else:
                l = mid + 1
        return l
