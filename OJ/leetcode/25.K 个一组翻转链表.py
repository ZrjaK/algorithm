# 题目：25.K 个一组翻转链表
# 难度：HARD
# 最后提交：2022-09-04 17:19:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        end = head
        while end:
            c += 1
            if c == k:
                break
            end = end.next
        if c < k or k == 1:
            return head
        while head != end:
            nxt = head.next
            head.next = end.next
            end.next = head
            head = nxt
        c = 0
        while end:
            c += 1
            if c == k:
                break
            end = end.next
        end.next = self.reverseKGroup(end.next, k)
        return head