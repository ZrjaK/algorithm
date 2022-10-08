# 题目：1219.黄金矿工
# 难度：MEDIUM
# 最后提交：2022-09-12 14:33:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def p(i, j):
            res = grid[i][j]
            t = grid[i][j]
            grid[i][j] = 0
            for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0<=x<m and 0<=y<n and grid[x][y]:
                    res = max(res, t+p(x, y))
            grid[i][j] = t
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, p(i, j))
        return res