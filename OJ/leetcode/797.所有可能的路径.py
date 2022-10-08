# 题目：797.所有可能的路径
# 难度：MEDIUM
# 最后提交：2022-08-01 17:40:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        @cache
        def p(i):
            if i == n-1:
                return [[n-1]]
            res = []
            for nxt in graph[i]:
                for r in p(nxt):
                    res.append([i] + r)
            return res
        return p(0)