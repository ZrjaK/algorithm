# 题目：1382.将二叉搜索树变平衡
# 难度：MEDIUM
# 最后提交：2022-08-20 04:14:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        h = []
        def p(node):
            if not node:
                return
            p(node.left)
            h.append(node.val)
            p(node.right)
        p(root)
        def b(l, r):
            mid = l+r>>1
            res = TreeNode(h[mid])
            if l <= mid-1:
                res.left = b(l, mid-1)
            if mid+1 <= r:
                res.right = b(mid+1, r)
            return res


        return b(0, len(h)-1)