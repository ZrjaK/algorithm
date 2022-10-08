# 题目：427.建立四叉树
# 难度：MEDIUM
# 最后提交：2022-09-12 13:07:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        t = sum(sum(i) for i in grid)
        if t == n**2:
            return Node(1, True)
        if t == 0:
            return Node(0, True)
        return Node(1, False, 
                self.construct([grid[i][:n//2] for i in range(n//2)]),
                self.construct([grid[i][n//2:] for i in range(n//2)]),
                self.construct([grid[i][:n//2] for i in range(n//2, n)]),
                self.construct([grid[i][n//2:] for i in range(n//2, n)]))