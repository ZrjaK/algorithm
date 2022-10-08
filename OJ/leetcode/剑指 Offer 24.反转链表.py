# 题目：剑指 Offer 24.反转链表
# 难度：EASY
# 最后提交：2022-10-01 16:49:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = ListNode(next=head)
        pre, cur = p, head
        while cur:
            pre, cur.next, cur = cur, pre, cur.next
        head.next = None
        return pre