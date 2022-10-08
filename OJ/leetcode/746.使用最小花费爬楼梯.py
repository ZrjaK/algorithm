# 题目：746.使用最小花费爬楼梯
# 难度：EASY
# 最后提交：2021-10-24 11:22:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])