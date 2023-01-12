# 题目：面试题 16.19.水域大小
# 难度：MEDIUM
# 最后提交：2023-01-06 09:25:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        D8 = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        n, m = len(land), len(land[0])
        dsu = DisjointSetUnion(n*m)
        for x in range(n):
            for y in range(m):
                for dx, dy in D8:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m and land[x][y] == land[nx][ny] == 0:
                        dsu.union(x*m+y, nx*m+ny)
        l = set()
        for i in range(n):
            for j in range(m):
                if not land[i][j]:
                    l.add(dsu.find(i*m+j))
        return sorted([dsu.size[i] for i in l])

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
 
    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
 
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
 
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
 
    def set_size(self, a):
        return self.size[self.find(a)]
 
    def __len__(self):
        return self.num_sets