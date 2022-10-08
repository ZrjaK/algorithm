# 题目：965.单值二叉树
# 难度：EASY
# 最后提交：2022-04-08 18:40:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        res = set()
        def p(node):
            if not node:
                return
            res.add(node.val)
            p(node.left)
            p(node.right)
        p(root)
        return len(res) == 1