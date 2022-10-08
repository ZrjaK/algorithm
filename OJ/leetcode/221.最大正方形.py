# 题目：221.最大正方形
# 难度：MEDIUM
# 最后提交：2022-06-22 20:02:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m < 1:
            return 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        ans = max(max(i) for i in dp)
        return ans**2