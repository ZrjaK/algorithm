# 题目：1039.多边形三角剖分的最低得分
# 难度：MEDIUM
# 最后提交：2022-07-23 21:52:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def p(l, r):
            if r-l < 2:
                return 0
            if r-l == 2:
                return values[l] * values[l+1] * values[r]
            res = 1e99
            for i in range(l+1, r):
                res = min(res, p(l, i) + p(i, r) + values[l]*values[i]*values[r])
            return res
        p.cache_clear()
        return p(0, n-1)