# 题目：2493.将节点分成尽可能多的组
# 难度：HARD
# 最后提交：2022-12-04 19:46:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        d = defaultdict(list)
        uf = UnionFind(n+1)
        for i, j in edges:
            uf.union(i, j)
            d[i].append(j)
            d[j].append(i)
        color = [0] * (n+1)
        for i in range(1, n+1):
            if not color[i]:
                color[i] = 1
                q = deque([i])
                while q:
                    u = q.popleft()
                    for v in d[u]:
                        if not color[v]:
                            color[v] = -color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return -1
        ans = defaultdict(int)
        def bfs(x):
            res = 0
            q = deque([(1, x)])
            vis = set([x])
            while q:
                s, u = q.popleft()
                res = max(res, s)
                for v in d[u]:
                    if v not in vis:
                        vis.add(v)
                        q.append((s+1, v))
            return res
        for i in range(1, n+1):
            ans[uf.find(i)] = max(ans[uf.find(i)], bfs(i))
        return sum(ans.values())

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
