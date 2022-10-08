# 题目：1559.二维网格图中探测环
# 难度：MEDIUM
# 最后提交：2022-08-17 21:46:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        parent = list(range(m*n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        for i in range(m):
            for j in range(n):
                if i+1 < m and grid[i][j] == grid[i+1][j]:
                    if find(n*i+j) == find(n*(i+1)+j):
                        return True
                    union(n*i+j, n*(i+1)+j)
                if j+1 < n and grid[i][j] == grid[i][j+1]:
                    if find(n*i+j) == find(n*i+j+1):
                        return True
                    union(n*i+j, n*i+j+1)
        return False
                
                    