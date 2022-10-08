# 题目：112.路径总和
# 难度：EASY
# 最后提交：2022-07-25 16:25:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def p(node, target):
            if not node:
                return False
            if not node.left and not node.right:
                return node.val == target
            return p(node.left, target-node.val) or p(node.right, target-node.val)
        return p(root, targetSum)