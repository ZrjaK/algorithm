# 题目：剑指 Offer II 099.最小路径之和
# 难度：MEDIUM
# 最后提交：2022-10-10 09:38:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def p(i, j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            res = 1e99
            if i + 1 < m:
                res = min(res, grid[i][j] + p(i+1, j))
            if j + 1 < n:
                res = min(res, grid[i][j] + p(i, j+1))
            return res
        return p(0, 0)