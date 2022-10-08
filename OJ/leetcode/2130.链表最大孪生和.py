# 题目：2130.链表最大孪生和
# 难度：MEDIUM
# 最后提交：2022-04-08 11:52:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return max(a[i]+a[-i-1] for i in range(len(a)//2))