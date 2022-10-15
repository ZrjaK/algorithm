# 题目：剑指 Offer II 118.多余的边
# 难度：MEDIUM
# 最后提交：2022-10-10 22:01:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        ans = []
        for i, j in edges:
            if uf.find(i) == uf.find(j):
                ans = [i, j]
            else:
                uf.union(i, j)
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
