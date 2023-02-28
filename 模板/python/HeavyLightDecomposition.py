class HeavyLightDecomposition:
    def __init__(self, G, root=0):
        self.G = G
        self.depth = [0] * len(G)
        self.down = [-1] * len(G)
        self.up = [-1] * len(G)
        self.nxt = [root] * len(G)
        self.par = [root] * len(G)
        self.dfs_sz(root)
        self.dfs_hld(root)
    
    def dfs_sz(self, v):
        stack = [v]
        size = [1] * len(self.G)
        while stack:
            v = stack.pop()
            if v >= 0:
                if len(self.G[v]) >= 2 and self.G[v][-1] == self.par[v]:
                    self.G[v][-1], self.G[v][-2] = self.G[v][-2], self.G[v][-1]
                for i, nv in enumerate(self.G[v]):
                    if nv == self.par[v]:
                        continue
                    self.depth[nv] = self.depth[v] + 1
                    self.par[nv] = v
                    stack.append(i)
                    stack.append(~nv)
                    stack.append(nv)
            else:
                nv = ~v
                v = self.par[nv]
                i = stack.pop()
                size[v] += size[nv]
                if size[nv] > size[self.G[v][-1]]:
                    self.G[v][-1], self.G[v][i] = self.G[v][i], self.G[v][-1]
        
    def dfs_hld(self, v):
        id = 0
        stack = [~v, v]
        while stack:
            v = stack.pop()
            if v >= 0:
                self.down[v] = id
                id += 1
                for nv in self.G[v]:
                    if nv == self.par[v]:
                        continue
                    if nv == self.G[v][-1]:
                        self.nxt[nv] = self.nxt[v]
                    else:
                        self.nxt[nv] = nv
                    stack.append(~nv)
                    stack.append(nv)
            else:
                self.up[~v] = id
                id += 1
                
    def lca(self, a, b):
        while self.nxt[a] != self.nxt[b]:
            if self.down[a] < self.down[b]:
                a, b = b, a
            a = self.par[self.nxt[a]]
        if self.depth[a] < self.depth[b]:
            return a
        else:
            return b