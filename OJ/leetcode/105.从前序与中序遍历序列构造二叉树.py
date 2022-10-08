# 题目：105.从前序与中序遍历序列构造二叉树
# 难度：MEDIUM
# 最后提交：2022-09-13 09:35:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        t = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+t], inorder[:t])
        root.right = self.buildTree(preorder[1+t:], inorder[t+1:])
        return root
