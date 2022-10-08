# 题目：617.合并二叉树
# 难度：EASY
# 最后提交：2022-07-29 16:36:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            node = TreeNode(node1.val+node2.val)
            node.left = merge(node1.left, node2.left)
            node.right = merge(node1.right, node2.right)
            return node
        return merge(root1, root2)