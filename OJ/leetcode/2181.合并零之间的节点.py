# 题目：2181.合并零之间的节点
# 难度：MEDIUM
# 最后提交：2022-04-05 18:53:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ne = cur.next
        s = 0
        while ne:
            if s == 0:
                cur = cur.next
            if ne.val == 0:
                cur.val = s
                s = 0
            else:
                s += ne.val
            ne = ne.next
        cur.next = None
        return head.next