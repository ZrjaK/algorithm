# 题目：剑指 Offer II 056.二叉搜索树中两个节点之和
# 难度：EASY
# 最后提交：2022-10-07 11:55:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        v = set()
        ans = False
        def p(node):
            nonlocal ans
            if not node:
                return
            p(node.left)
            ans |= (k-node.val) in v
            v.add(node.val)
            p(node.right)
        p(root)
        return ans