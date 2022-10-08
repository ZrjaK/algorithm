# 题目：257.二叉树的所有路径
# 难度：EASY
# 最后提交：2022-08-17 23:45:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def p(node, l):
            if node.left:
                p(node.left, l+[node.val])
            if node.right:
                p(node.right, l+[node.val])
            if not node.left and not node.right:
                res.append(l+[node.val])
        p(root, [])
        return ["->".join([str(j) for j in i]) for i in res]