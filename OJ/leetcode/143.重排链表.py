# 题目：143.重排链表
# 难度：MEDIUM
# 最后提交：2022-09-04 17:01:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        h = deque()
        p = head
        while p:
            h.append(p)
            p = p.next
        p = h.popleft()
        k = 1
        while h:
            if k:
                p.next = h.pop()
            else:
                p.next = h.popleft()
            k ^= 1
            p = p.next
        p.next = None
        return head