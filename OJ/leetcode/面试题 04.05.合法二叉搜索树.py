# 题目：面试题 04.05.合法二叉搜索树
# 难度：MEDIUM
# 最后提交：2023-01-06 13:42:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        h = []
        def p(node):
            if not node:
                return
            p(node.left)
            h.append(node.val)
            p(node.right)
        p(root)
        return len(h) == len(set(h)) and h == sorted(h)