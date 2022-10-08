# 题目：剑指 Offer 22.链表中倒数第k个节点
# 难度：EASY
# 最后提交：2022-10-01 16:45:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        t = head
        c = 0
        while t:
            t = t.next
            c += 1
        for _ in range(c-k):
            head = head.next
        return head