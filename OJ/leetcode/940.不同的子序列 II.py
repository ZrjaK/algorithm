# 题目：940.不同的子序列 II
# 难度：HARD
# 最后提交：2022-10-14 01:36:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

MOD=int(1e9+7)
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        last = {}
        dp = [0] * (n+1)
        dp[-1] = 1
        for i in range(n):
            dp[i] = dp[i-1] * 2
            if s[i] in last:
                dp[i] -= dp[last[s[i]]-1]
            last[s[i]] = i
        return (dp[n-1]-1) % int(1e9+7)