# 题目：669.修剪二叉搜索树
# 难度：MEDIUM
# 最后提交：2022-09-10 00:14:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def p(node):
            if not node:
                return
            while node.left and node.left.val < low:
                node.left = node.left.right
            while node.right and node.right.val > high:
                node.right = node.right.left
            p(node.left)
            p(node.right)
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                break
        
        p(root)
        return root