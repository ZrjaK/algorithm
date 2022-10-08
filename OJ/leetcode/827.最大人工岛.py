# 题目：827.最大人工岛
# 难度：HARD
# 最后提交：2022-09-18 14:03:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = list(range(n*n+n))
        cnt = [0] * (n*n+n)
        for i in range(n):
            for j in range(n):
                cnt[i*n+j] = grid[i][j]
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            i, j = find(i), find(j)
            if i != j:
                cnt[i], cnt[j] = 0, cnt[i]+cnt[j]
            parent[i] = parent[j]
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    continue
                for x, y in [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]:
                    if 0<=x<n and 0<=y<n and grid[x][y] == 1:
                        union(x*n+y, i*n+j)
        ans = max(cnt[i] for i in range(n*n+n))
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                t =  []
                v = set()
                for x, y in [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]:
                    if 0<=x<n and 0<=y<n and grid[x][y] == 1:
                        v.add(find(x*n+y))
                for k in v:
                    t.append(cnt[k])
                t.sort(reverse=True)
                ans = max(ans, 1+sum(t+[0]))
        return ans