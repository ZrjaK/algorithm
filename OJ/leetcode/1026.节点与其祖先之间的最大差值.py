# 题目：1026.节点与其祖先之间的最大差值
# 难度：MEDIUM
# 最后提交：2022-08-19 18:14:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def p(node):
            nonlocal ans
            l = p(node.left) if node.left else [node.val, node.val]
            r = p(node.right) if node.right else [node.val, node.val]
            res = [min(l[0], r[0], node.val), max(l[1], r[1], node.val)]
            ans = max(ans, abs(res[0]-node.val), abs(res[1]-node.val))
            return res
        p(root)
        return ans