# 题目：1319.连通网络的操作次数
# 难度：MEDIUM
# 最后提交：2022-08-17 21:01:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        c = 0
        for i, j in connections:
            if find(i) == find(j):
                c += 1
                continue
            union(i, j)
        root = set()
        for i in range(n):
            root.add(find(i))
        return len(root)-1 if c >= len(root)-1 else -1