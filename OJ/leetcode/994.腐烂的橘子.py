# 题目：994.腐烂的橘子
# 难度：MEDIUM
# 最后提交：2022-08-04 02:25:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    pq.append((0, i, j))
        ans = 0
        while pq:
            t, x, y = heappop(pq)
            ans = max(ans, t)
            for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=dx<m and 0<=dy<n and grid[dx][dy] == 1:
                    grid[dx][dy] = 2
                    heappush(pq, (t+1, dx, dy))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    return -1
        return ans