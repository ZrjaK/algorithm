# 题目：1617.统计子树中城市之间最大距离
# 难度：HARD
# 最后提交：2022-09-28 11:52:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        dst = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            q = deque([[0, i]])
            v = set()
            while q:
                s, t = q.popleft()
                if t in v:
                    continue
                v.add(t)
                dst[i][t] = s
                for j in d[t]:
                    q.append((s+1, j))
        ans = [0] * (n-1)
        f = set()
        for mask in range(1<<n+1):
            uf = UnionFind(n+1)
            for i in range(1, n+1):
                if not mask>>i & 1:
                    continue
                for j in d[i]:
                    if mask>>j & 1:
                        uf.union(i, j)
            v = set()
            for i in range(1, n+1):
                if not mask>>i & 1:
                    continue
                v.add(uf.find(i))
            if len(v) != 1:
                continue
            if mask>>1 in f:
                continue
            f.add(mask>>1)
            t = -1
            for i in range(1, n+1):
                if not mask>>i & 1:
                    continue
                for j in range(1, n+1):
                    if mask>>j & 1:
                        t = max(t, dst[i][j])
            if t > 0:
                ans[t-1] += 1
        return ans

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
