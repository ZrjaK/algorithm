# 题目：1771.由子序列构造的最长回文串的长度
# 难度：HARD
# 最后提交：2022-09-22 16:56:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    if i < len(word1) and j >= len(word1):
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return ans