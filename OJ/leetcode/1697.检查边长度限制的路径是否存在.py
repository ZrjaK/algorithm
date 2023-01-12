# 题目：1697.检查边长度限制的路径是否存在
# 难度：HARD
# 最后提交：2022-12-14 01:58:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = [[i, j, k, l] for i, (j, k, l) in enumerate(queries)]
        queries.sort(key=lambda x: x[3])
        edgeList.sort(key=lambda x: -x[2])
        uf = UnionFind(n)
        ans = [False] * len(queries)
        for i, j, k, l in queries:
            while edgeList and edgeList[-1][2] < l:
                x, y, _ = edgeList.pop()
                uf.union(x, y)
            ans[i] = uf.find(j) == uf.find(k)
        return ans

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.part = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x, y = self.find(i), self.find(j)
        if x != y:
            self.size[y] += self.size[x]
            self.parent[x] = self.parent[y]
            self.part -= 1