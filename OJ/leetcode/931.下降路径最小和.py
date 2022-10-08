# 题目：931.下降路径最小和
# 难度：MEDIUM
# 最后提交：2022-07-09 01:23:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def p(i, j):
            if i == m:
                return 0
            res = p(i+1, j)
            if j > 0:
                res = min(res, p(i+1, j-1))
            if j < n-1:
                res = min(res, p(i+1, j+1))
            return res + matrix[i][j]
        return min(p(0, j) for j in range(n))
            