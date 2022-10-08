# 题目：剑指 Offer 27.二叉树的镜像
# 难度：EASY
# 最后提交：2022-10-02 22:25:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def p(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            p(node.left)
            p(node.right)
        p(root)
        return root