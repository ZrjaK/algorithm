# 题目：2331.计算布尔二叉树的值
# 难度：EASY
# 最后提交：2022-07-09 22:34:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def p(node):
            if node.left == None:
                return bool(node.val)
            l = p(node.left)
            r = p(node.right)
            if node.val == 2:
                return l or r
            if node.val == 3:
                return l and r
            
        return p(root)
            