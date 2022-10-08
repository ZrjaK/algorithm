# 题目：802.找到最终的安全状态
# 难度：MEDIUM
# 最后提交：2022-08-01 18:22:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = set()
        @cache
        def p(i):
            if i in visited:
                return False
            visited.add(i)
            res = True
            for nxt in graph[i]:
                res &= p(nxt)
            return res
        res = []
        for i in range(n):
            if p(i):
                res.append(i)
        return res
