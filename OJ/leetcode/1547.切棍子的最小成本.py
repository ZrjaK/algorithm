# 题目：1547.切棍子的最小成本
# 难度：HARD
# 最后提交：2022-09-19 16:13:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        @cache
        def p(x1, x2, l, r):
            if l == r:
                return 0
            res = 1e99
            for i in range(l, r):
                res = min(res, p(x1, cuts[i], l, i) + p(cuts[i], x2, i+1, r))
            return res + x2-x1
        return p(0, n, 0, len(cuts))
