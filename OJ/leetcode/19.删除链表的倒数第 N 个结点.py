# 题目：19.删除链表的倒数第 N 个结点
# 难度：MEDIUM
# 最后提交：2022-04-04 22:16:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head