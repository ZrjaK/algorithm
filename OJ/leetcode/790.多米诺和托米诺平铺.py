# 题目：790.多米诺和托米诺平铺
# 难度：MEDIUM
# 最后提交：2022-11-12 16:24:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numTilings(self, n: int) -> int:
        if n < 2:
            return n
        dp = [[0] * 3 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-2][0]
            dp[i][1] = dp[i-1][2] + dp[i-2][0]
            dp[i][2] = dp[i-1][1] + dp[i-2][0]
        return dp[-1][0] % int(1e9+7)