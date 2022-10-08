# 题目：剑指 Offer 26.树的子结构
# 难度：MEDIUM
# 最后提交：2022-10-01 16:55:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        def check(node1, node2):
            if not node2:
                return True
            if not node1:
                return node1 == node2 == None
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)
        def p(node):
            if not node:
                return False
            if check(node, B):
                return True
            return p(node.left) or p(node.right)
        return p(A)