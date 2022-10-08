# 题目：234.回文链表
# 难度：EASY
# 最后提交：2022-10-05 15:07:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        h = []
        while head:
            h.append(head.val)
            head = head.next
        return h == h[::-1]