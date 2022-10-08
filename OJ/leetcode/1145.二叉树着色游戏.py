# 题目：1145.二叉树着色游戏
# 难度：MEDIUM
# 最后提交：2022-04-05 04:08:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def findx(node):
            if node == None:
                return None
            if node.val == x:
                return node
            l, r = findx(node.left), findx(node.right)
            if l:
                return l
            if r:
                return r
        def getc(node):
            if node == None:
                return 0
            return 1 + getc(node.left) + getc(node.right)

        xroot = findx(root)
        left, right = getc(xroot.left), getc(xroot.right)
        return (left>n//2) or (right>n//2) or (n-1-left-right>n//2)
