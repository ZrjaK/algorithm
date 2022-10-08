# 题目：589.N 叉树的前序遍历
# 难度：EASY
# 最后提交：2022-08-18 01:12:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def p(node):
            if not node:
                return
            res.append(node.val)
            for c in node.children:
                p(c)
        p(root)
        return res
