# 题目：121.买卖股票的最佳时机
# 难度：EASY
# 最后提交：2022-09-03 01:52:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p = 999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p