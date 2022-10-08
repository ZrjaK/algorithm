# 题目：2088.统计农场中肥沃金字塔的数目
# 难度：HARD
# 最后提交：2022-09-19 13:32:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def p(i, j):
            if not grid[i][j]:
                return 0
            res = 0
            if i+1<m and j-1>=0 and j+1<n:
                if grid[i+1][j-1] == grid[i+1][j] == grid[i+1][j+1] == 1:
                    res += 1
                    res += min(p(i+1, j-1), p(i+1, j), p(i+1, j+1))
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                res += p(i, j)
        p.cache_clear()
        grid = grid[::-1]
        for i in range(m):
            for j in range(n):
                res += p(i, j)
        return res