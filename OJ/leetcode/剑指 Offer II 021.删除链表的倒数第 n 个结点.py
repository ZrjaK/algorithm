# 题目：剑指 Offer II 021.删除链表的倒数第 n 个结点
# 难度：MEDIUM
# 最后提交：2022-10-05 14:56:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        c = 0
        p = head
        while p:
            p = p.next
            c += 1
        pre = ListNode(next=head)
        p = pre
        while c - n:
            c -= 1
            p = p.next
        p.next = p.next.next
        return pre.next