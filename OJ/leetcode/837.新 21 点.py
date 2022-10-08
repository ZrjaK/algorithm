# 题目：837.新 21 点
# 难度：MEDIUM
# 最后提交：2022-05-20 14:42:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp= [0] * (k+maxPts)
        s = 0
        for i in range(k, k+maxPts):
            dp[i] = 1 if i <= n else 0
            s += dp[i]
        for i in range(k-1,-1,-1):
            dp[i] = s / maxPts
            s += dp[i] - dp[i+maxPts]
        return dp[0]
