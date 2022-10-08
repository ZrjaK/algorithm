# 题目：142.环形链表 II
# 难度：MEDIUM
# 最后提交：2022-06-02 19:39:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if fast == slow:
                p = head
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        return None