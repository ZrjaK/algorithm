# 题目：938.二叉搜索树的范围和
# 难度：EASY
# 最后提交：2022-08-18 01:24:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0]
        def p(node):
            if not node:
                return
            if low <= node.val <= high:
                res[0] += node.val
            p(node.left)
            p(node.right)
        p(root)
        return res[0]
