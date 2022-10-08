# 题目：1627.带阈值的图连通性
# 难度：HARD
# 最后提交：2022-09-26 10:35:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n+1))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        for i in range(1, n+1):
            for j in range(1, ceil(i**0.5)+1):
                if i % j == 0:
                    if j > threshold:
                        union(i, j)
                    if i//j > threshold:
                        union(i//j, i)
        ans = []
        for i, j in queries:
            ans.append(find(i) == find(j))
        return ans
