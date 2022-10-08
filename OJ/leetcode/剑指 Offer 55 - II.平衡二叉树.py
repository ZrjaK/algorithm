# 题目：剑指 Offer 55 - II.平衡二叉树
# 难度：EASY
# 最后提交：2022-10-03 20:16:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def p(node):
            if not node:
                return [True, 0]
            l = p(node.left)
            r = p(node.right)
            if not l[0] or not r[0]:
                return [False, 0]
            if abs(l[1]-r[1]) > 1:
                return [False, 0]
            return [True, 1 + max(l[1], r[1])]
        return p(root)[0]