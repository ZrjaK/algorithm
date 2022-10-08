# 题目：988.从叶结点开始的最小字符串
# 难度：MEDIUM
# 最后提交：2022-08-19 17:43:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        def p(node, s):
            if not node:
                return
            t = chr(node.val+97) + s
            if not node.left and not node.right:
                res.append(t)
            p(node.left, t)
            p(node.right, t)
        p(root, "")
        res.sort()
        return res[0]