# 题目：623.在二叉树中增加一行
# 难度：MEDIUM
# 最后提交：2022-04-19 06:43:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root, None)
        res = []
        def p(node, d):
            if not node:
                return
            if d == depth-1:
                res.append(node)
            p(node.left, d+1)
            p(node.right, d+1)
        p(root, 1)
        for node in res:
            l = TreeNode(val, node.left, None)
            r = TreeNode(val, None, node.right)
            node.left = l
            node.right = r
        return root