# 题目：2421.好路径的数目
# 难度：HARD
# 最后提交：2022-09-25 12:34:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]), reverse=True)
        c = defaultdict(list)
        parent = list(range(n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        for i in range(n):
            c[vals[i]].append(i)
        ans = 0
        for val in sorted(c):
            while edges and max(vals[edges[-1][0]], vals[edges[-1][1]]) <= val:
                union(edges[-1][0], edges[-1][1])
                edges.pop()
            t = defaultdict(int)
            for i in c[val]:
                t[find(i)] += 1
            for i in t.values():
                ans += i + i * (i-1) // 2
        return ans
                        
        