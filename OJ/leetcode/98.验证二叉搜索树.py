# 题目：98.验证二叉搜索树
# 难度：MEDIUM
# 最后提交：2022-08-18 01:46:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def p(node):
            if not node:
                return
            p(node.left)
            res.append(node.val)
            p(node.right)
        p(root)
        return len(res) == len(set(res)) and res == sorted(res)
            