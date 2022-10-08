# 题目：147.对链表进行插入排序
# 难度：MEDIUM
# 最后提交：2022-08-27 14:53:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = head
        while cur:
            pre = dummy
            while pre.next and pre.next.val <= cur.val:
                pre = pre.next
            tmp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = tmp
        return dummy.next