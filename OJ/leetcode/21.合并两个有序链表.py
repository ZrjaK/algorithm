# 题目：21.合并两个有序链表
# 难度：EASY
# 最后提交：2022-09-07 15:18:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        c = res
        while list1 and list2:
            if list1.val < list2.val:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c = c.next
        if list1:
            c.next = list1
        if list2:
            c.next = list2
        return res.next