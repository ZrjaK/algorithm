# 题目：剑指 Offer II 078.合并排序链表
# 难度：HARD
# 最后提交：2022-10-08 14:44:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for i, node in enumerate(lists):
            if node:
                heappush(pq, [node.val, i, node])
        res = ListNode()
        p = res
        while pq:
            _, i, node = heappop(pq)
            p.next = node
            p = p.next
            if not node.next:
                continue
            heappush(pq, [node.next.val, i, node.next])
        return res.next