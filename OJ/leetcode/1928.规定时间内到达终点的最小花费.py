# 题目：1928.规定时间内到达终点的最小花费
# 难度：HARD
# 最后提交：2022-10-14 18:44:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        d = defaultdict(list)
        for i, j, c in edges:
            d[i].append((j, c))
            d[j].append((i, c))
        @cache
        def p(i, rest):
            if rest < 0:
                return 1e99
            if i == n-1:
                return passingFees[i]
            res = 1e99
            for nxt, c in d[i]:
                res = min(res, passingFees[i] + p(nxt, rest-c))
            return res
        res = p(0, maxTime)
        return res if res < 1e90 else -1