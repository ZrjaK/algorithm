# 题目：235.二叉搜索树的最近公共祖先
# 难度：MEDIUM
# 最后提交：2022-08-17 23:39:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node.val > q.val and node.val > p.val:
                return dfs(node.left)
            elif node.val < q.val and node.val < p.val:
                return dfs(node.right)
            else:
                return node
        return dfs(root)
            