# 题目：剑指 Offer II 077.链表排序
# 难度：MEDIUM
# 最后提交：2022-10-08 14:39:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            r = mergeSort(slow.next)
            slow.next = None
            l = mergeSort(head)
            return merge(l, r)
        def merge(l, r):
            res = ListNode()
            p = res
            while l and r:
                if l.val < r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
            if l:
                p.next = l
            if r:
                p.next = r
            return res.next
        return mergeSort(head)