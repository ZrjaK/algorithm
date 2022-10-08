# 题目：684.冗余连接
# 难度：MEDIUM
# 最后提交：2022-08-15 16:12:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        res = []
        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                res = [node1, node2]
        
        return res