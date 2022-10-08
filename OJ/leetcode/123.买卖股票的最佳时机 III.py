# 题目：123.买卖股票的最佳时机 III
# 难度：HARD
# 最后提交：2022-04-01 20:32:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = -1e99
        sell1 = sell2 = 0
        for i in prices:
            buy1 = max(buy1, -i)
            sell1 = max(sell1, buy1 + i)
            buy2 = max(buy2, sell1 - i)
            sell2 = max(sell2, buy2 + i)
        return sell2