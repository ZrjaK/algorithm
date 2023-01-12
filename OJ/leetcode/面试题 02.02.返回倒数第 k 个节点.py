# 题目：面试题 02.02.返回倒数第 k 个节点
# 难度：EASY
# 最后提交：2022-12-11 19:49:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        p = head
        for _ in range(n-k):
            p = p.next
        return p.val