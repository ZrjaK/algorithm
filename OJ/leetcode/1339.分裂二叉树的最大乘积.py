# 题目：1339.分裂二叉树的最大乘积
# 难度：MEDIUM
# 最后提交：2022-08-20 04:04:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s = 0
        d = {}
        def p(node):
            nonlocal s
            if not node:
                return 0
            s += node.val
            l = p(node.left)
            r = p(node.right)
            d[node] = node.val + l + r
            return node.val + l + r
        p(root)
        ans = 0
        for i in d.keys():
            if i != root:
                ans = max(ans, d[i]*(s-d[i]))
        return ans % int(1e9+7)