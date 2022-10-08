# 题目：947.移除最多的同行或同列石头
# 难度：MEDIUM
# 最后提交：2022-08-17 16:26:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = 10000
        parent=list(range(2*n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = find(j)
        for i, j in stones:
            union(i, j+n)
        root = set()
        for i, j in stones:
            root.add(find(i))
        return len(stones) - len(root)