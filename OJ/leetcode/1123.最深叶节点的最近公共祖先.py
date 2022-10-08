# 题目：1123.最深叶节点的最近公共祖先
# 难度：MEDIUM
# 最后提交：2022-08-06 01:59:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def p(node):
            if not node:
                return None
            ld, rd = maxD(node.left), maxD(node.right)
            if ld == rd:
                return node
            elif ld > rd:
                return p(node.left)
            else:
                return p(node.right)
        @cache
        def maxD(node):
            if not node:
                return 0
            return 1 + max(maxD(node.left), maxD(node.right))
        return p(root)