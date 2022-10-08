# 题目：剑指 Offer 07.重建二叉树
# 难度：MEDIUM
# 最后提交：2022-09-30 11:08:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        t = inorder.index(preorder[0])
        return TreeNode(preorder[0], 
                    self.buildTree(preorder[1:1+t], inorder[:t]),
                    self.buildTree(preorder[1+t:], inorder[t+1:]))