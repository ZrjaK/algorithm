# 题目：543.二叉树的直径
# 难度：EASY
# 最后提交：2022-08-18 00:58:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        @cache
        def p(node):
            if not node:
                return 0
            res = 1 + max(p(node.left), p(node.right))
            ans[0] = max(ans[0], p(node.left)+p(node.right))
            return res
        p(root)
        return ans[0]