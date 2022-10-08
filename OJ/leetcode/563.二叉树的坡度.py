# 题目：563.二叉树的坡度
# 难度：EASY
# 最后提交：2022-08-18 01:03:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def p(node):
            if not node:
                return 0
            s1 = p(node.left)
            s2 = p(node.right)
            ans[0] += abs(s1-s2)
            t = node.val
            node.val = abs(s1-s2)
            return t + s1 + s2
        p(root)
        return ans[0]
            