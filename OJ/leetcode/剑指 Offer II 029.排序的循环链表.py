# 题目：剑指 Offer II 029.排序的循环链表
# 难度：MEDIUM
# 最后提交：2022-10-05 21:10:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            f = Node(insertVal)
            f.next = f
            return f
        p = head
        v = set()
        h = []
        while p not in v and p.val <= p.next.val:
            v.add(p)
            p = p.next
        p = p.next
        v.clear()
        while p not in v:
            h.append(p)
            v.add(p)
            p = p.next
        for i in range(len(h)):
            if h[i].val > insertVal:
                h = h[:i] + [Node(insertVal)] + h[i:]
                break
        else:
            h.append(Node(insertVal))
        for i in range(len(h)-1):
            h[i].next = h[i+1]
        h[-1].next = h[0]
        return head