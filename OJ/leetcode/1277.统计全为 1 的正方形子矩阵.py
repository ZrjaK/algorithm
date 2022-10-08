# 题目：1277.统计全为 1 的正方形子矩阵
# 难度：MEDIUM
# 最后提交：2022-07-14 18:10:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    ans += dp[i][j]
        return ans