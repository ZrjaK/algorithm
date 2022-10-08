# 题目：230.二叉搜索树中第K小的元素
# 难度：MEDIUM
# 最后提交：2022-04-13 08:59:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def p(node):
            if node == None:
                return
            p(node.left)
            a.append(node.val)
            p(node.right)
        p(root)
        return a[k-1]