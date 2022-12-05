# 题目：2487.从链表中移除节点
# 难度：MEDIUM
# 最后提交：2022-11-27 12:26:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = []
        p = head
        while p:
            h.append(p.val)
            p = p.next
        q = []
        for i in h:
            while q and q[-1] < i:
                q.pop()
            q.append(i)
        res = ListNode()
        p = res
        for i in q:
            p.next = ListNode(i)
            p = p.next
        return res.next