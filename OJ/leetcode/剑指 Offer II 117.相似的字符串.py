# 题目：剑指 Offer II 117.相似的字符串
# 难度：HARD
# 最后提交：2022-10-10 21:59:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(s, t):
            res = len([1 for i, j in zip(s, t) if i != j])
            return res == 0 or res == 2
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if check(strs[i], strs[j]):
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
