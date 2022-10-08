# 题目：226.翻转二叉树
# 难度：EASY
# 最后提交：2022-07-27 16:34:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def p(node):
            if not node:
                return node
            node.left, node.right = p(node.right), p(node.left)
            return node
        return p(root)