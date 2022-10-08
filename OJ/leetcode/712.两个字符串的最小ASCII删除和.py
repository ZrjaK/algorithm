# 题目：712.两个字符串的最小ASCII删除和
# 难度：MEDIUM
# 最后提交：2022-07-07 00:05:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, len(s2)+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(ord(s1[i-1])+dp[i-1][j], ord(s2[j-1])+dp[i][j-1])
        return dp[-1][-1]