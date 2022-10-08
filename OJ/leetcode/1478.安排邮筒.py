# 题目：1478.安排邮筒
# 难度：HARD
# 最后提交：2022-09-23 08:45:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        cost = [[0] * n for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                cost[i][j] = cost[i+1][j-1] + houses[j] - houses[i]
        @cache
        def p(i, rest):
            if i == n:
                return 0 if not rest else 1e99
            if not rest:
                return 1e99
            res = 1e99
            for j in range(i, n):
                res = min(res, cost[i][j]+p(j+1, rest-1))
            return res
        return p(0, k)