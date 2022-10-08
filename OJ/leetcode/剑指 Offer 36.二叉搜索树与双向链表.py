# 题目：剑指 Offer 36.二叉搜索树与双向链表
# 难度：MEDIUM
# 最后提交：2022-10-03 10:37:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        def p(node):
            if not node:
                return [None, None]
            l, r = p(node.left), p(node.right)
            if l[1]:
                l[1].right = node
                node.left = l[1]
            if r[0]:
                r[0].left = node
                node.right = r[0]
            res = [l[0], r[1]]
            if not res[0]:
                res[0] = node
            if not res[1]:
                res[1] = node
            return res
        l, r = p(root)
        l.left, r.right = r, l
        return l