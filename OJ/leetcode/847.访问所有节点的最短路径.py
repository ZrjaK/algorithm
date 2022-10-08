# 题目：847.访问所有节点的最短路径
# 难度：HARD
# 最后提交：2022-09-23 15:05:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        d = defaultdict(list)
        for i in range(n):
            for j in graph[i]:
                d[i].append(j)
                d[j].append(i)
        v = defaultdict(lambda: 1e99)
        # @cache
        def p(state, i, s):
            v[state, i] = s
            if state == (1<<n)-1 or s > 2*n:
                return s
            res = 1e99
            for j in d[i]:
                if v[state|1<<i, j] > s+1:
                    res = min(res, p(state|1<<i, j, s+1))
            return res
        res = min(p(0, i, -1) for i in range(n))
        # p.cache_clear()
        if res > 1e90:
            return 0
        return res