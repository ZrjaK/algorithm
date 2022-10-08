# 题目：951.翻转等价二叉树
# 难度：MEDIUM
# 最后提交：2022-08-19 14:19:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def p(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            p1 = p(node1.left, node2.left) and p(node1.right, node2.right)
            p2 = p(node1.right, node2.left) and p(node1.left, node2.right)
            return p1 or p2
        return p(root1, root2)