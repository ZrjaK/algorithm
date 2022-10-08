# 题目：剑指 Offer 18.删除链表的节点
# 难度：EASY
# 最后提交：2022-09-30 23:36:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        t = ListNode(next=head)
        f = t
        while t and t.next:
            if t.next.val == val:
               t.next = t.next.next
               break
            t = t.next

        return f.next 