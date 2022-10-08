# 题目：329.矩阵中的最长递增路径
# 难度：HARD
# 最后提交：2022-03-26 09:56:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def process(matrix: List[List[int]], row: int, col: int, dp: List[List[int]]) -> int:
            if dp[row][col]:
                return dp[row][col]
            next1, next2, next3, next4 = 0, 0, 0, 0
            if row > 0 and matrix[row-1][col] > matrix[row][col]:
                next1 = process(matrix, row-1, col, dp)
            if row+1 < len(matrix) and matrix[row+1][col] > matrix[row][col]:
                next2 = process(matrix, row+1, col, dp)
            if col > 0 and matrix[row][col-1] > matrix[row][col]:
                next3 = process(matrix, row, col-1, dp)
            if col+1 < len(matrix[0]) and matrix[row][col+1] > matrix[row][col]:
                next4 = process(matrix, row, col+1, dp)
            dp[row][col] = max([next1, next2, next3, next4]) + 1
            return dp[row][col]
 
        n = len(matrix)
        m = len(matrix[0])
        ma = 0
        for i in range(n):
            for j in range(m):
                dp = [[0] * m for _ in range(n)]
                ma = max(ma, process(matrix, i, j, dp))
        return ma