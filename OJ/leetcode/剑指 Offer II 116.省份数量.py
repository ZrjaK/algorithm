# 题目：剑指 Offer II 116.省份数量
# 难度：MEDIUM
# 最后提交：2022-10-10 21:52:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.part

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
