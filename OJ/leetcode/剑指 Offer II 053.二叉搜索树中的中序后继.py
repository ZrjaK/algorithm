# 题目：剑指 Offer II 053.二叉搜索树中的中序后继
# 难度：MEDIUM
# 最后提交：2022-10-07 11:00:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        h = []
        def d(node):
            if not node:
                return
            d(node.left)
            h.append(node)
            d(node.right)
        d(root)
        for i in range(len(h)):
            if h[i].val == p.val:
                if i != len(h)-1:
                    return h[i+1]
                else:
                    return None