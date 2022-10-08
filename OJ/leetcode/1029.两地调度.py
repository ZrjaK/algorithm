# 题目：1029.两地调度
# 难度：MEDIUM
# 最后提交：2022-08-30 02:07:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x:x[0]-x[1])
        return sum(i[0] for i in costs[:n]) + sum(i[1] for i in costs[n:])