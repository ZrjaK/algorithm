# 题目：188.买卖股票的最佳时机 IV
# 难度：HARD
# 最后提交：2022-04-09 13:57:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        @lru_cache(None)
        def p(day, op, isBuy):
            if day == len(prices) - 1:
                return prices[day] if isBuy else 0
            if isBuy:
                return max(p(day+1, op, True), # 不买不卖
                            p(day+1, op, False) + prices[day]) # 只卖不买
            else:
                if op != 0:
                    return max(p(day+1, op-1, True) - prices[day],
                                p(day+1, op, False))
                else:
                    return p(day+1, op, False)
        return p(0, k, False)
