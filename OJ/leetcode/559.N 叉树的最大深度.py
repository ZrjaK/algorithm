# 题目：559.N 叉树的最大深度
# 难度：EASY
# 最后提交：2022-07-29 16:30:32 +0800 CST
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
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        res = 0
        for c in root.children:
            res = max(res, self.maxDepth(c))
        return 1 + res