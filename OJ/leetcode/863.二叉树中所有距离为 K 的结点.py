# 题目：863.二叉树中所有距离为 K 的结点
# 难度：MEDIUM
# 最后提交：2022-08-02 03:07:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = defaultdict(list)
        def p(node):
            if node.left:
                d[node.val].append(node.left.val)
                d[node.left.val].append(node.val)
                p(node.left)
            if node.right:
                d[node.val].append(node.right.val)
                d[node.right.val].append(node.val)
                p(node.right)
        p(root)
        dst = defaultdict(int)
        q = deque([[0, target.val]])
        while q:
            t, node = q.popleft()
            if node in dst:
                continue
            dst[node] = t
            for nxt in d[node]:
                q.append([t+1, nxt])
        res = []
        for i in dst.keys():
            if dst[i] == k:
                res.append(i)
        return res