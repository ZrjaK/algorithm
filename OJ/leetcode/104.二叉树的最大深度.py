# 题目：104.二叉树的最大深度
# 难度：EASY
# 最后提交：2022-07-25 16:19:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def p(node):
            if not node:
                return 0
            return 1 + max(p(node.left), p(node.right))
        return p(root)