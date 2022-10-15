# 题目：剑指 Offer II 105.岛屿的最大面积
# 难度：MEDIUM
# 最后提交：2022-10-10 12:26:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n+n)
        for x in range(m):
            for y in range(n):
                if not grid[x][y]:
                    continue
                for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]:
                        uf.union(x*n+y, nx*n+ny)
        return max([0] + [uf.size[uf.find(i*n+j)] for i in range(m) for j in range(n) if grid[i][j]])


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
