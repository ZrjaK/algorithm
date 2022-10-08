# 题目：1361.验证二叉树
# 难度：MEDIUM
# 最后提交：2022-08-17 21:12:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = list(range(n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        v = set()
        for i in range(n):
            if leftChild[i] != -1:
                if find(i) == find(leftChild[i]) or leftChild[i] in v:
                    return False
                else:
                    v.add(leftChild[i])
                    union(i, leftChild[i])
            if rightChild[i] != -1:
                if find(i) == find(rightChild[i]) or rightChild[i] in v:
                    return False
                else:
                    v.add(rightChild[i])
                    union(i, rightChild[i])
        root = set()
        for i in range(n):
            root.add(find(i))
        return len(root) == 1