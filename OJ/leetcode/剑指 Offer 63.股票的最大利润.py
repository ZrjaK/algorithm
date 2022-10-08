# 题目：剑指 Offer 63.股票的最大利润
# 难度：MEDIUM
# 最后提交：2022-10-03 21:04:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from sortedcontainers import SortedList
        s = SortedList()
        ans = 0
        for i in prices:
            if s.bisect_left(i) != 0:
                ans = max(ans, i-s[0])
            s.add(i)
        return ans