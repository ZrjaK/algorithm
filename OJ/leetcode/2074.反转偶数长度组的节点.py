# 题目：2074.反转偶数长度组的节点
# 难度：MEDIUM
# 最后提交：2022-10-22 15:03:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = []
        for i in range(1, 10**5):
            if not head:
                break
            t = []
            for _ in range(i):
                if not head:
                    break
                if head:
                    t.append(head)
                    head = head.next
            h.append(t)
        for i in range(len(h)):
            if len(h[i]) % 2 == 0:
                h[i] = h[i][::-1]
        pre = ListNode()
        p = pre
        for i in h:
            for j in i:
                p.next = ListNode(j.val)
                p = p.next
        return pre.next