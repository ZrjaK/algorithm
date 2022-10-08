# 题目：2095.删除链表的中间节点
# 难度：MEDIUM
# 最后提交：2022-06-21 12:53:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow == head:
            return head.next
        p = head
        while p and p.next != slow:
            p = p.next
        p.next = p.next.next
        return head