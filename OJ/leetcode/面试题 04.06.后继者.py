# 题目：面试题 04.06.后继者
# 难度：MEDIUM
# 最后提交：2022-10-22 15:12:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        h = []
        def pr(node):
            if not node:
                return
            pr(node.left)
            h.append(node)
            pr(node.right)
        pr(root)
        h.append(None)
        for i in range(len(h)-1):
            if h[i] == p:
                return h[i+1]