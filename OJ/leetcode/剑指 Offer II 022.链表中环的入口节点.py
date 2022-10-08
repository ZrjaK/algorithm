# 题目：剑指 Offer II 022.链表中环的入口节点
# 难度：MEDIUM
# 最后提交：2022-10-05 15:01:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        v = set()
        while head:
            if head in v:
                return head
            v.add(head)
            head = head.next
        return None