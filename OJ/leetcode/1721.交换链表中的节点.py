# 题目：1721.交换链表中的节点
# 难度：MEDIUM
# 最后提交：2022-06-12 13:30:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        c = 1
        n1 = n2 = head
        while c < k:
            n1 = n1.next
            c += 1
        c = 0
        while c < n-k:
            n2 = n2.next
            c += 1
        n1.val, n2.val = n2.val, n1.val
        return head
