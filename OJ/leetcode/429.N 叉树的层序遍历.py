# 题目：429.N 叉树的层序遍历
# 难度：MEDIUM
# 最后提交：2022-04-08 01:16:10 +0800 CST
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def p(node, d):
            if not node:
                return
            if len(res) <= d:
                res.append([])
            res[d].append(node.val)
            for c in node.children:
                p(c,d+1)
        p(root, 0)
        return res