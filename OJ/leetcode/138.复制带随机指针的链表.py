# 题目：138.复制带随机指针的链表
# 难度：MEDIUM
# 最后提交：2022-10-02 23:14:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        p = head
        while p:
            t = Node(p.val, p.next)
            p.next = t
            p = t.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        head = p = head.next
        while p and p.next:
            nxt = p.next
            p.next = p.next.next
            p = nxt
        return head