# 题目：1475.商品折扣后的最终价格
# 难度：EASY
# 最后提交：2022-09-01 19:31:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                t = stack.pop()
                ans[t] = prices[t] - prices[i]
            stack.append(i)
        while stack:
            t = stack.pop()
            ans[t] = prices[t]
        return ans