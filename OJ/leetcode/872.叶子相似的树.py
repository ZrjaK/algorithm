# 题目：872.叶子相似的树
# 难度：EASY
# 最后提交：2022-08-18 01:17:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def p(node, res):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
            p(node.left, res)
            p(node.right, res)
        r1 = []
        r2 = []
        p(root1, r1)
        p(root2, r2)
        return r1 == r2