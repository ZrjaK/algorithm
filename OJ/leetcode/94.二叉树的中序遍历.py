# 题目：94.二叉树的中序遍历
# 难度：EASY
# 最后提交：2022-08-15 02:43:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def p(node):
            if not node:
                return
            p(node.left)
            res.append(node.val)
            p(node.right)
        p(root)
        return res