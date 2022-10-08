# 题目：1155.掷骰子的N种方法
# 难度：MEDIUM
# 最后提交：2022-04-05 05:11:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target+1) for _ in range(n+1)]
        for i in range(1,min(k+1,target+1)):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                if j-k-1 >= 0:
                    dp[i][j] -= dp[i-1][j-k-1]
                dp[i][j] %= 1e9+7
        return int(dp[n][target])