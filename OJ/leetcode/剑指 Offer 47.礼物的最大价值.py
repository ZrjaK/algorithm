# 题目：剑指 Offer 47.礼物的最大价值
# 难度：MEDIUM
# 最后提交：2023-03-08 08:13:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def p(i, j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            res = 0
            if i + 1 < m:
                res = max(res, p(i+1, j))
            if j + 1 < n:
                res = max(res, p(i, j+1))
            return res + grid[i][j]
        return p(0, 0)