# 题目：654.最大二叉树
# 难度：MEDIUM
# 最后提交：2022-09-02 13:58:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def p(arr):
            if not arr:
                return None
            i = arr.index(max(arr))
            return TreeNode(arr[i], p(arr[:i]), p(arr[i+1:]))
        return p(nums)