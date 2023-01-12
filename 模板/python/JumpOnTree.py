class JumpOnTree:
    def __init__(self, edges, root=0):
        self.n = len(edges)
        self.edges = edges
        self.root = root
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1] * self.n
        self.depth[self.root] = 0
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()
 
    def dfs(self):
        stack = [self.root]
        while stack:
            u = stack.pop()
            for v in self.edges[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    stack.append(v)
 
    def doubling(self):
        for i in range(1, self.logn):
            for u in range(self.n):
                p = self.parent[i - 1][u]
                if p != -1:
                    self.parent[i][u] = self.parent[i - 1][p]
 
    def lca(self, u, v):
        du = self.depth[u]
        dv = self.depth[v]
        if du > dv:
            du, dv = dv, du
            u, v = v, u
 
        d = dv - du
        i = 0
        while d > 0:
            if d & 1:
                v = self.parent[i][v]
            d >>= 1
            i += 1
        if u == v:
            return u
 
        logn = (du - 1).bit_length()
        for i in range(logn - 1, -1, -1):
            pu = self.parent[i][u]
            pv = self.parent[i][v]
            if pu != pv:
                u = pu
                v = pv
        return self.parent[0][u]
 
    def jump(self, u, v, k):
        if k == 0:
            return u
        p = self.lca(u, v)
        d1 = self.depth[u] - self.depth[p]
        d2 = self.depth[v] - self.depth[p]
        if d1 + d2 < k:
            return -1
        if k <= d1:
            d = k
        else:
            u = v
            d = d1 + d2 - k
        i = 0
        while d > 0:
            if d & 1:
                u = self.parent[i][u]
            d >>= 1
            i += 1
        return u
 
    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]