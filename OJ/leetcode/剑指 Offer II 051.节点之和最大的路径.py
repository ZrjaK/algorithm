# 题目：剑指 Offer II 051.节点之和最大的路径
# 难度：HARD
# 最后提交：2022-10-07 10:55:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = -1e99
        def p(node):
            nonlocal ans
            if not node:
                return 0
            l, r = p(node.left), p(node.right)
            ans = max(ans, max([0, l, r, l+r]) + node.val)
            return max([0, l, r]) + node.val
        p(root)
        return ans