# 题目：1594.矩阵的最大非负积
# 难度：MEDIUM
# 最后提交：2022-07-18 22:52:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @cache
        def p(i, j):
            if i == n-1 and j == m-1:
                return [grid[i][j], grid[i][j]]
            res1 = [-1e99, 1e99]
            res2 = [-1e99, 1e99]
            if i < n-1:
                res1 = p(i+1, j)
            if j < m-1:
                res2 = p(i, j+1)
            x = grid[i][j]
            if x > 0:
                return [max(res1[0], res2[0]) * x, min(res1[1], res2[1]) * x]
            elif x < 0:
                return [min(res1[1], res2[1]) * x, max(res1[0], res2[0]) * x]
            else:
                return [0, 0]
        res = p(0, 0)
        print(res)
        return res[0] % int(1e9+7) if res[0] >= 0 else -1