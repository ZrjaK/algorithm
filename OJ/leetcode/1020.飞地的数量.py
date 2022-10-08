# 题目：1020.飞地的数量
# 难度：MEDIUM
# 最后提交：2022-08-04 02:38:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([])
        for i in range(m):
            for j in [0, n-1]:
                if grid[i][j]:
                    grid[i][j] = 0
                    q.append([i, j])
        for i in [0, m-1]:
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    q.append([i, j])

        while q:
            x, y = q.popleft()
            for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=dx<m and 0<=dy<n and grid[dx][dy]:
                    grid[dx][dy] = 0
                    q.append([dx, dy])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += 1
        return ans