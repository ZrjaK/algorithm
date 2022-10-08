# 题目：1325.删除给定值的叶子节点
# 难度：MEDIUM
# 最后提交：2022-08-20 03:55:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def p(node):
            if not node:
                return
            p(node.left)
            p(node.right)
            if node.left and not node.left.left and not node.left.right and node.left.val == target:
                node.left = None
            if node.right and not node.right.left and not node.right.right and node.right.val == target:
                node.right = None
        t = TreeNode(-1, root)
        p(t)
        return t.left
            