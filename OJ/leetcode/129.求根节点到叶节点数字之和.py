# 题目：129.求根节点到叶节点数字之和
# 难度：MEDIUM
# 最后提交：2022-08-18 16:19:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def p(node, v):
            if not node:
                return
            if not node.left and not node.right:
                ans[0] += 10*v + node.val
            p(node.left, 10*v+node.val)
            p(node.right, 10*v+node.val)
        p(root,0)
        return ans[0]