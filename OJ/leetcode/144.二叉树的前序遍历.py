# 题目：144.二叉树的前序遍历
# 难度：EASY
# 最后提交：2022-08-17 23:25:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def p(node):
            if not node:
                return
            res.append(node.val)
            p(node.left)
            p(node.right)
        p(root)
        return res