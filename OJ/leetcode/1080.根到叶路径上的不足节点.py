# 题目：1080.根到叶路径上的不足节点
# 难度：MEDIUM
# 最后提交：2022-08-20 03:45:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        res = TreeNode(left=root)
        def p(node, v):
            if not node:
                return 0
            l = p(node.left, v + node.val) if node.left else -1e99
            r = p(node.right, v + node.val) if node.right else -1e99
            if not node.left and not node.right:
                l = r = 0
            if l + v + node.val < limit:
                node.left = None
            if r + v + node.val < limit:
                node.right = None
            return max(l, r) + node.val
        p(res, 0)
        return res.left