# 题目：2328.网格图中递增路径的数目
# 难度：HARD
# 最后提交：2022-07-03 11:34:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def p(i, j):
            res = 1
            if i != m-1 and grid[i][j] < grid[i+1][j]:
                res += p(i+1, j)
            if i != 0 and grid[i][j] < grid[i-1][j]:
                res += p(i-1, j)
            if j != n-1 and grid[i][j] < grid[i][j+1]:
                res += p(i, j+1)
            if j != 0 and grid[i][j] < grid[i][j-1]:
                res += p(i, j-1)
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                res += p(i, j)
        return res % int(1e9 + 7)