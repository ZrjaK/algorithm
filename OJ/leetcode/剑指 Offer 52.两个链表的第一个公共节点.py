# 题目：剑指 Offer 52.两个链表的第一个公共节点
# 难度：EASY
# 最后提交：2022-10-03 18:59:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = l2 = 0
        p = headA
        while p:
            l1 += 1
            p = p.next
        p = headB
        while p:
            l2 += 1
            p = p.next
        if l1 > l2:
            headA, headB = headB, headA
            l1, l2 = l2, l1
        t = l2 - l1
        while t:
            headB = headB.next
            t -= 1
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA