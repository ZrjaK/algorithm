# 题目：剑指 Offer II 028.展平多级双向链表
# 难度：MEDIUM
# 最后提交：2022-10-05 20:55:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def p(node):
            cur = node
            tail = node
            while cur:
                if cur.child:
                    t = p(cur.child)
                    if cur.next:
                        cur.next.prev = t[1] 
                    t[1].next = cur.next
                    cur.next, t[0].prev = t[0], cur
                    cur.child = None
                if not cur.next:
                    tail = cur
                cur = cur.next
            return [node, tail]
        return p(head)[0]