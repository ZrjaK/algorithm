# 题目：剑指 Offer II 110.所有路径
# 难度：MEDIUM
# 最后提交：2022-10-10 17:02:19 +0800 CST
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