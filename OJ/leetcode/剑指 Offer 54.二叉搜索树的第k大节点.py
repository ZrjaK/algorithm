# 题目：剑指 Offer 54.二叉搜索树的第k大节点
# 难度：EASY
# 最后提交：2022-10-03 19:02:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        h = []
        def p(node):
            if not node:
                return
            p(node.left)
            h.append(node.val)
            p(node.right)
        p(root)
        return h[-k]