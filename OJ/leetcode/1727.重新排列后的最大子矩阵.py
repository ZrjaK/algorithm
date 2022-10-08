# 题目：1727.重新排列后的最大子矩阵
# 难度：MEDIUM
# 最后提交：2022-08-31 19:27:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        res = 0
        for i in range(m):
            matrix[i].sort()
            for j in range(n-1, -1, -1):
                res = max(res, matrix[i][j] * (n-j))
        return res