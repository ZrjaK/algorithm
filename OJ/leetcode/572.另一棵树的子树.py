# 题目：572.另一棵树的子树
# 难度：EASY
# 最后提交：2022-08-18 01:10:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        h = []
        def p(node):
            if not node:
                return 
            if node.val == subRoot.val:
                h.append(node)
            p(node.left)
            p(node.right)
        p(root)
        if not h:
            return False
        def p2(node, r):
            if not node:
                return
            p2(node.left, r)
            r.append(node.val)
            p2(node.right, r)
        r2 = []
        p2(subRoot, r2)
        for n in h:
            r1 = []
            p2(n, r1)
            if r1 == r2:
                return True
        return False
        
