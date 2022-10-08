# 题目：558.四叉树交集
# 难度：MEDIUM
# 最后提交：2022-09-13 12:45:38 +0800 CST
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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val == 1:
                return quadTree1
            else:
                return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val == 1:
                return quadTree2
            else:
                return quadTree1
        res = Node(0, False, 
                    self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                    self.intersect(quadTree1.topRight, quadTree2.topRight),
                    self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                    self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))
        if res.topLeft.isLeaf and res.topRight.isLeaf and res.bottomLeft.isLeaf and res.bottomRight.isLeaf and res.topLeft.val == res.topRight.val == res.bottomLeft.val == res.bottomRight.val:
            res = Node(res.topLeft.val, True)
        return res