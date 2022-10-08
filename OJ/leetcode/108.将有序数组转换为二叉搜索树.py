# 题目：108.将有序数组转换为二叉搜索树
# 难度：EASY
# 最后提交：2022-09-13 09:29:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        return TreeNode(nums[n//2], 
                self.sortedArrayToBST(nums[:n//2]),
                self.sortedArrayToBST(nums[n//2+1:]))