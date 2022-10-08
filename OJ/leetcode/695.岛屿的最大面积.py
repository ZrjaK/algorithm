# 题目：695.岛屿的最大面积
# 难度：MEDIUM
# 最后提交：2022-07-30 00:55:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                q = deque([[i, j]])
                c = 0
                while q:
                    x, y = q.popleft()
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    c += 1
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]:
                            q.append([x+dx, y+dy])
                ans = max(ans, c)
        return ans
