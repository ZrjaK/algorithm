# 题目：100.相同的树
# 难度：EASY
# 最后提交：2022-07-25 16:11:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def d(node, r):
            if not node:
                r.append(None)
                return
            r.append(node.val)
            d(node.left, r)
            d(node.right, r)
        r1 = []
        r2 = []
        d(p, r1)
        d(q, r2)
        return r1 == r2