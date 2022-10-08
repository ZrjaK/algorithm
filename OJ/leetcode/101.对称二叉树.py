# 题目：101.对称二叉树
# 难度：EASY
# 最后提交：2022-07-25 16:18:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def p(node1, node2):
            if not node1 and not node2:
                return True
            if not (node1 and node2) or node1.val != node2.val:
                return False
            return p(node1.left, node2.right) and p(node1.right, node2.left)
        return p(root.left, root.right)