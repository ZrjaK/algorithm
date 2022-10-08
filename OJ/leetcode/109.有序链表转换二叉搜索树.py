# 题目：109.有序链表转换二叉搜索树
# 难度：MEDIUM
# 最后提交：2022-09-13 09:42:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        h = []
        while head:
            h.append(head.val)
            head = head.next
        def p(nums):
            if not nums:
                return None
            n = len(nums)
            return TreeNode(nums[n//2], 
                    p(nums[:n//2]),
                    p(nums[n//2+1:]))
        return p(h)