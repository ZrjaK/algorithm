# 题目：剑指 Offer II 088.爬楼梯的最少成本
# 难度：EASY
# 最后提交：2022-10-09 16:49:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def p(i):
            if i >= n:
                return 0
            return cost[i] + min(p(i+1), p(i+2))
        return min(p(0), p(1))