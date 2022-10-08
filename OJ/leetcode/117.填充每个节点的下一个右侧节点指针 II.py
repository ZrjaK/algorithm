# 题目：117.填充每个节点的下一个右侧节点指针 II
# 难度：MEDIUM
# 最后提交：2022-07-25 17:03:59 +0800 CST
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
    def connect(self, root: 'Node') -> 'Node':
        def p(node):
            if not node:
                return
            if node.right:
                n = node.next
                while n:
                    if node.right.next:
                        break
                    node.right.next = n.left
                    if not node.right.next:
                        node.right.next = n.right
                    n = n.next
            if node.left:
                node.left.next = node.right
                n = node.next
                while n:
                    if node.left.next:
                        break
                    node.left.next = n.left
                    if not node.left.next:
                        node.left.next = n.right
                    n = n.next
            p(node.right)
            p(node.left)
        p(root)
        return root