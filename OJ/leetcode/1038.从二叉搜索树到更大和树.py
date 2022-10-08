# 题目：1038.从二叉搜索树到更大和树
# 难度：MEDIUM
# 最后提交：2022-03-25 23:37:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        l = SortedList()
        def p1(node: TreeNode):
            if node:
                l.add(node.val)
            else:
                return
            if node.left:
                p1(node.left)
            if node.right:
                p1(node.right)
        def p2(node: TreeNode):
            if node:
                i = l.index(node.val)
                node.val = sum(l[i:])
            else:
                return
            if node.left:
                p2(node.left)
            if node.right:
                p2(node.right) 
        p1(root)
        p2(root)
        return root
