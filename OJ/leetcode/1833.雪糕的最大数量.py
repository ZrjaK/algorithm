# 题目：1833.雪糕的最大数量
# 难度：MEDIUM
# 最后提交：2022-08-31 19:30:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
            else:
                return i
        return len(costs)