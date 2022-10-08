# 题目：110.平衡二叉树
# 难度：EASY
# 最后提交：2022-08-17 23:25:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def p(node):
            if not node:
                return [True, 0]
            r1 = p(node.left)
            r2 = p(node.right)
            if abs(r1[1]-r2[1]) > 1:
                return [False, 0]
            return [r1[0] and r2[0], 1 + max(r1[1], r2[1])]
        return p(root)[0]