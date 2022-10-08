# 题目：2192.有向无环图中一个节点的所有祖先
# 难度：MEDIUM
# 最后提交：2022-08-13 17:02:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        indegree = [0] * n
        for i, j in edges:
            d[j].append(i)
            indegree[i] += 1
        ans = [[] for _ in range(n)]
        def p(i):
            if ans[i]:
                return ans[i]
            res = []
            for c in d[i]:
                res += p(c) + [c]
            ans[i] = list(set(res))
            ans[i].sort()
            return ans[i]
        for i in range(n):
            if not indegree[i]:
                ans[i] = p(i)
        return [i for i in ans]