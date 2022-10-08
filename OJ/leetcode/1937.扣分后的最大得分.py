# 题目：1937.扣分后的最大得分
# 难度：MEDIUM
# 最后提交：2022-09-19 14:31:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        @cache
        def p(i):
            if i == m-1:
                return points[i]
            res = 0
            f = p(i+1)
            ma = -1e99
            res = [0] * n
            for j in range(n):
                ma = max(ma, f[j]+j)
                res[j] = max(res[j], ma + points[i][j] - j)
            ma = -1e99
            for j in range(n-1, -1, -1):
                ma = max(ma, f[j]-j)
                res[j] = max(res[j], ma + points[i][j] + j)
            return res
        return max(p(0))