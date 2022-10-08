# 题目：116.填充每个节点的下一个右侧节点指针
# 难度：MEDIUM
# 最后提交：2022-07-25 16:31:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        res = []
        c = 1
        nxt = 0
        t = []
        q = deque([root])
        while q:
            node = q.popleft()
            c -= 1
            t.append(node)
            if node.left:
                q.append(node.left)
                nxt += 1
            if node.right:
                q.append(node.right)
                nxt += 1
            if c == 0:
                res.append(t)
                c = nxt
                nxt = 0
                t = []
        for row in res:
            for i in range(len(row)-1):
                row[i].next = row[i+1]
        return root