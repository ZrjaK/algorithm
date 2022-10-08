# 题目：剑指 Offer II 025.链表中的两数相加
# 难度：MEDIUM
# 最后提交：2022-10-05 15:05:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = "", ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        t = str(int(n1)+int(n2))
        h = ListNode(int(t[0]))
        c = h
        for i in t[1:]:
            c.next = ListNode(int(i))
            c = c.next
        return h