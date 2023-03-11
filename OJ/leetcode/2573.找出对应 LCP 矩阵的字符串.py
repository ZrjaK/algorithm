# 题目：2573.找出对应 LCP 矩阵的字符串
# 难度：HARD
# 最后提交：2023-02-21 20:15:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        vis = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j and lcp[i][j] == 0:
                    return ""
                if lcp[i][j] != lcp[j][i]:
                    return ""
        dsu = DisjointSetUnion(n)
        for i in range(n):
            for j in range(n):
                if vis[i][j]:
                    continue
                if lcp[i][j]:
                    c = lcp[i][j]
                    x, y = i, j
                    while x < n and y < n:
                        vis[x][y] = 1
                        if lcp[x][y] == 0:
                            break
                        dsu.union(x, y)
                        if lcp[x][y] != c:
                            return ""
                        c -= 1
                        x += 1
                        y += 1
                    if c > 0:
                        return ""
        ans = [""] * n
        h = set()
        for i in range(n):
            h.add(dsu.find(i))
        if len(h) > 26:
            return ""
        h = sorted(h)
        d = defaultdict(int)
        c = 0
        for i in h:
            d[i] = chr(c+97)
            c += 1
        for i in range(n):
            ans[i] = d[dsu.find(i)]
        f = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1,-1,-1):
            for j in range(n - 1,-1,-1):
                if ans[i] == ans[j]:
                    f[i][j] = 1
                    if i + 1 < n and j + 1 < n:
                        f[i][j] += f[i + 1][j + 1]
        if f != lcp:
            return ""
        return "".join(ans)
        
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