# 题目：剑指 Offer 55 - I.二叉树的深度
# 难度：EASY
# 最后提交：2022-10-03 19:03:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def p(node):
            if not node:
                return 0
            return 1 + max(p(node.left), p(node.right))
        return p(root)