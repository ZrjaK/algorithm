# 题目：309.最佳买卖股票时机含冷冻期
# 难度：MEDIUM
# 最后提交：2022-06-23 12:44:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1]+prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1])
        return dp[n-1][0]