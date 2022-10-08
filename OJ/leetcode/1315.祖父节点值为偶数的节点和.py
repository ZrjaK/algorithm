# 题目：1315.祖父节点值为偶数的节点和
# 难度：MEDIUM
# 最后提交：2022-08-09 01:15:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        def p(node, i, j):
            if not node:
                return
            if not i:
                res[0] += node.val
            if node.val % 2 == 0:
                p(node.left, j-1, 1)
                p(node.right, j-1, 1)
            else:
                p(node.left, j-1, -1)
                p(node.right, j-1, -1)
        p(root, -1, -1)
        return res[0]