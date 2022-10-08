# 题目：132.分割回文串 II
# 难度：HARD
# 最后提交：2022-04-05 21:35:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCut(self, s: str) -> int:
        a = [[True] * len(s) for _ in s]
        for i in range(len(a)-1, -1, -1):
            for j in range(i+1, len(a)):
                if s[i] == s[j]:
                    a[i][j] = a[i+1][j-1]
                else:
                    a[i][j] = False
        dp = [1e99] * (len(s)+1)
        dp[-1] = 0
        for i in range(len(dp)-2, -1, -1):
            for j in range(i+1, len(s)+1):
                if a[i][j-1]:
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[0] - 1