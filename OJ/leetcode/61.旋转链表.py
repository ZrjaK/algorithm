# 题目：61.旋转链表
# 难度：MEDIUM
# 最后提交：2022-05-26 10:42:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        t = head
        n = 1
        while t.next:
            t = t.next
            n += 1
        k %= n
        p = head
        while k+1 < n:
            p = p.next
            k += 1
        t.next = head
        ret = p.next
        p.next = None
        return ret