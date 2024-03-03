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
def solve():
    n, m = map(int, input().split())
    dsu = DisjointSetUnion(n)
    d = [[] for _ in range(n)]
    x = y = -1
    EE = [[int(i) for i in input().split()] for _ in range(m)]
    E = {}
    for i, (u, v) in enumerate(EE):
        u -= 1
        v -= 1
        E[u, v] = E[v, u] = i + 1
        if dsu.find(u) == dsu.find(v):
            x, y = u, v
            break
        dsu.union(u, v)
        d[u].append(v)
        d[v].append(u)
    else:
        print(-1)
        return
    ans = []
    vis = [0] * n
    vis[x] = 1
    q = [x]
    while q:
        i = q.pop()
        if i >= 0:
            ans.append(i)
            if i == y:
                break
            for j in d[i]:
                if vis[j] == 0:
                    vis[j] = 1
                    q.append(~j)
                    q.append(j)
        else:
            ans.pop()
    ans = [E[ans[i], ans[i - 1]] for i in range(len(ans))]
    ans.sort()
    print(*ans)

for _ in range(int(input())):
    solve()

    