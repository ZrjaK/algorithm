# 题目：剑指 Offer II 091.粉刷房子
# 难度：MEDIUM
# 最后提交：2022-10-09 17:08:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @cache
        def p(i, pre):
            if i == n:
                return 0
            res = 1e99
            for j in range(3):
                if j != pre:
                    res = min(res, costs[i][j] + p(i+1, j))
            return res
        return p(0, -1)