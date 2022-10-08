# 题目：865.具有所有最深节点的最小子树
# 难度：MEDIUM
# 最后提交：2022-08-02 03:17:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
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