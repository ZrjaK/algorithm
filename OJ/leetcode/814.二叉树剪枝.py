# 题目：814.二叉树剪枝
# 难度：MEDIUM
# 最后提交：2022-08-19 14:14:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def p(node):
            if not node:
                return None
            res = node if node.val == 1 else None
            node.left = p(node.left)
            node.right = p(node.right)
            if node.left or node.right:
                res = node
            return res
        return p(root)
            