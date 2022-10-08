# 题目：671.二叉树中第二小的节点
# 难度：EASY
# 最后提交：2022-08-18 01:13:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def p(node):
            if not node:
                return
            s.add(node.val)
            p(node.left)
            p(node.right)
        p(root)
        if len(s) < 2:
            return -1
        return sorted(list(s))[1]