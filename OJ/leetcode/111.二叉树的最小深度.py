# 题目：111.二叉树的最小深度
# 难度：EASY
# 最后提交：2022-07-25 16:22:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def p(node):
            if not node:
                return 1e99
            if not node.left and not node.right:
                return 1
            return 1 + min(p(node.left), p(node.right))
        return p(root)