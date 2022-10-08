# 题目：LCP 67.装饰树
# 难度：MEDIUM
# 最后提交：2022-10-07 15:06:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def p(node):
            if not node:
                return
            l, r = node.left, node.right
            if l:
                node.left = TreeNode(-1, l)
            if r:
                node.right = TreeNode(-1, None, r)
            p(l)
            p(r)
        p(root)
        return root