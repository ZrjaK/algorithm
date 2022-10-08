# 题目：714.买卖股票的最佳时机含手续费
# 难度：MEDIUM
# 最后提交：2022-07-07 12:39:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1]+prices[i]-fee, dp[i-1][0])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]