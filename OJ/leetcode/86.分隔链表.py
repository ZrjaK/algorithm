# 题目：86.分隔链表
# 难度：MEDIUM
# 最后提交：2022-06-01 11:19:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1, h2 = ListNode(), ListNode()
        p = head
        p1 = h1
        p2 = h2
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p2.next = None
        p1.next = h2.next
        return h1.next