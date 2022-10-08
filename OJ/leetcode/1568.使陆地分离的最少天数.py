# 题目：1568.使陆地分离的最少天数
# 难度：HARD
# 最后提交：2022-09-24 23:19:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = list(range(m*n+n))
        cnt = [1] * (m*n+n)
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            x, y = find(i), find(j)
            if x != y:
                cnt[y] += cnt[x]
                parent[x] = parent[y]
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                for x, y in [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]:
                    if 0<=x<m and 0<=y<n and grid[x][y]:
                        union(i*n+j, x*n+y)
        a = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    a.add(find(i*n+j))
        if len(a) != 1:
            return 0
        
        dfn = [[0] * n for _ in range(m)]
        low = [[0] * n for _ in range(m)]
        index = 0
        ans = False
        v = set()
        stack = []
        def tarjan(i, j, father):
            nonlocal ans
            nonlocal index
            index += 1
            dfn[i][j] = low[i][j] = index
            v.add((i, j))
            stack.append((i, j))
            child = 0
            for x, y in [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]:
                if 0<=x<m and 0<=y<n and grid[x][y] and (x, y) != father:
                    if not dfn[x][y]:
                        child += 1
                        tarjan(x, y, (i, j))
                        low[i][j] = min(low[i][j], low[x][y])
                        if father != (-1, -1) and dfn[i][j] <= low[x][y]:
                            ans = True
                        elif parent == (-1, -1) and child >= 2:
                            ans = True
                    elif (x, y) in v:
                        low[i][j] = min(low[i][j], low[x][y])
            if dfn[i][j] == low[i][j]:
                lst = []
                while stack[-1] != (i, j):
                    lst.append(stack.pop())
                lst.append(stack.pop())
                for x, y in lst:
                    low[x][y] = low[i][j]

        a = list(a)
        if cnt[a[0]] == 1:
            return 1
        tarjan(a[0]//n, a[0]%n, (-1, -1))
        return 1 if ans else 2