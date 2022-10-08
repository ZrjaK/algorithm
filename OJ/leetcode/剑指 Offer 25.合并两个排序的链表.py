# 题目：剑指 Offer 25.合并两个排序的链表
# 难度：EASY
# 最后提交：2022-10-01 16:51:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        f = ListNode()
        p = f
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        while l1:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2:
            p.next = l2
            p = p.next
            l2 = l2.next
        return f.next