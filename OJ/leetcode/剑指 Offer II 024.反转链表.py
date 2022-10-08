# 题目：剑指 Offer II 024.反转链表
# 难度：EASY
# 最后提交：2022-10-05 15:04:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = ListNode(next=head)
        cur = head
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        head.next = None
        return pre