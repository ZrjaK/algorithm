# 题目：749.隔离病毒
# 难度：HARD
# 最后提交：2022-09-27 11:44:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
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
                if isInfected[i][j]:
                    for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                        if 0<=x<m and 0<=y<n and isInfected[x][y]:
                            union(i*n+j, x*n+y)
        ans = 0
        while 1:
            part = defaultdict(set)
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        part[find(i*n+j)].add(i*n+j)
            infect = defaultdict(int)
            c = defaultdict(set)
            for root in part:
                for f in part[root]:
                    x, y = f//n, f % n
                    for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                        if 0<=nx<m and 0<=ny<n and isInfected[nx][ny] == 0:
                            infect[root] += 1
                            c[root].add(nx*n+ny)
            if not infect:
                break
            for root in sorted(infect, key=lambda x:len(c[x]), reverse=True):
                ans += infect[root]
                for f in part[root]:
                    x, y = f//n, f % n
                    isInfected[x][y] = -1
                c[root] = set()
                break
            for root in c:
                for f in c[root]:
                    x, y = f//n, f % n
                    isInfected[x][y] = 1
                    for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                        if 0<=nx<m and 0<=ny<n and isInfected[nx][ny] == 1:
                            union(nx*n+ny, x*n+y)
        return ans