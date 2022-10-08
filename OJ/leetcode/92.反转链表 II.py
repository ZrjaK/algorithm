# 题目：92.反转链表 II
# 难度：MEDIUM
# 最后提交：2022-03-21 05:57:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        stack = []
        p = head
        i = 1
        while p:
            if i >= left and i <= right:
                stack.append(p.val)
            i += 1
            p = p.next
        p = head
        i = 1
        while p:
            if i >= left and i <= right:
                p.val = stack.pop()
            i += 1
            p = p.next
        return head

