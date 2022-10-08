# 题目：106.从中序与后序遍历序列构造二叉树
# 难度：MEDIUM
# 最后提交：2022-09-13 09:40:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        t = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:t], postorder[:t])
        root.right = self.buildTree(inorder[t+1:], postorder[t:-1])
        return root