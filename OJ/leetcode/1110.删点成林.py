# 题目：1110.删点成林
# 难度：MEDIUM
# 最后提交：2022-08-20 03:52:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        s = set(to_delete)
        def p(node):
            if not node:
                return
            p(node.left)
            p(node.right)
            if node.left and node.left.val in s:
                node.left = None
            if node.right and node.right.val in s:
                node.right = None
            if node.val in s:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
        t = TreeNode(-1,root)
        s.add(-1)
        p(t)
        return res
