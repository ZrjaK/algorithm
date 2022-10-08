# 题目：687.最长同值路径
# 难度：MEDIUM
# 最后提交：2022-09-02 14:17:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = {}
        @cache
        def p(node):
            if not node:
                return 0
            l = 0
            if node.left and node.left.val == node.val:
                l = 1 + p(node.left)
            r = 0
            if node.right and node.right.val == node.val:
                r = 1 + p(node.right)
            d[node] = l+r
            p(node.left)
            p(node.right)
            return max(l, r)
        p(root)
        return max(d.values())