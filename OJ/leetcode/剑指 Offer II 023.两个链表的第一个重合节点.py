# 题目：剑指 Offer II 023.两个链表的第一个重合节点
# 难度：EASY
# 最后提交：2022-10-05 15:02:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def detectCycle(head: ListNode) -> ListNode:
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
        p = headA
        while p and p.next:
            p = p.next
        p.next = headB
        ret = detectCycle(headA)
        p.next = None
        return ret