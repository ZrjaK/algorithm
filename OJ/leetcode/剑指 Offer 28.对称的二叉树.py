# 题目：剑指 Offer 28.对称的二叉树
# 难度：EASY
# 最后提交：2022-10-02 22:29:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def p(node1, node2):
            if not node1 or not node2:
                return node1 == node2 == None
            if node1.val != node2.val:
                return False
            return p(node1.left, node2.right) and p(node1.right, node2.left)
        return p(root.left, root.right)