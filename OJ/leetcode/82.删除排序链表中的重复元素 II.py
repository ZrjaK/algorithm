# 题目：82.删除排序链表中的重复元素 II
# 难度：MEDIUM
# 最后提交：2022-05-27 09:52:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = defaultdict(int)
        cur = head
        while cur:
            d[cur.val] += 1
            cur = cur.next
        pre = head
        while pre and d[pre.val] > 1:
            pre = pre.next
        head = pre
        while pre:
            while pre.next and d[pre.next.val] > 1:
                pre.next = pre.next.next
            pre = pre.next
        return head