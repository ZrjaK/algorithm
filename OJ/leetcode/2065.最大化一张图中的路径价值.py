# 题目：2065.最大化一张图中的路径价值
# 难度：HARD
# 最后提交：2022-09-22 12:13:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        d = defaultdict(list)
        c = [[0] * n for _ in range(n)]
        for i, j, k in edges:
            d[i].append(j)
            d[j].append(i)
            c[i][j] = k
            c[j][i] = k
        @cache
        def p(i, rest, state):
            res = -1e99
            state |= 1<<i
            for j in d[i]:
                if rest >= c[i][j]:
                    res = max(res, p(j, rest-c[i][j], state))
            if i == 0:
                res = max(res, sum(values[j] for j in range(n) if state>>j & 1))
            return res
        return p(0, maxTime, 0)