# 题目：1457.二叉树中的伪回文路径
# 难度：MEDIUM
# 最后提交：2022-08-10 18:39:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = [0]
        def p(node, t):
            n = t ^ (1<<node.val)
            if not node.left and not node.right:
                if not n or not n & (n-1):
                    ans[0] += 1
            if node.left:
                p(node.left, n)
            if node.right:
                p(node.right, n)
        p(root, 0)
        return ans[0]
