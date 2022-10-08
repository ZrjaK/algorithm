# 题目：2144.打折购买糖果的最小开销
# 难度：EASY
# 最后提交：2022-10-03 15:01:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost[i] for i in range(len(cost)) if i % 3 != 2)