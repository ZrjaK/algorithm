# 题目：404.左叶子之和
# 难度：EASY
# 最后提交：2022-07-29 16:26:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        if root.left and not root.left.left and not root.left.right:
            res += root.left.val
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)