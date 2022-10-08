# 题目：1473.粉刷房子 III
# 难度：HARD
# 最后提交：2022-09-16 10:07:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def p(i, t, pre):
            if t > target:
                return 1e99
            if i == m:
                if t == target:
                    return 0
                else:
                    return 1e99
            if houses[i]:
                return p(i+1, t + (houses[i] != pre), houses[i])
            res = 1e99
            for j in range(n):
                res = min(res, cost[i][j]+p(i+1, t + (j+1 != pre), j+1))
            return res
        res = p(0, 0, -1)
        return res if res < 1e90 else -1