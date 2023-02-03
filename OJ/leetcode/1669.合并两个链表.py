# 题目：1669.合并两个链表
# 难度：MEDIUM
# 最后提交：2023-01-30 01:23:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1 = []
        p = list1
        while p:
            h1.append(p.val)
            p = p.next
        h2 = []
        p = list2
        while p:
            h2.append(p.val)
            p = p.next
        h = h1[:a] + h2 + h1[b+1:]
        res = ListNode()
        p = res
        for i in h:
            p.next = ListNode(i)
            p = p.next
        return res.next