# 题目：655.输出二叉树
# 难度：MEDIUM
# 最后提交：2022-07-29 03:19:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def h(node):
            if not node:
                return 0
            return 1 + max(h(node.left), h(node.right))
        height = h(root)
        res = [[""] * (2**height-1) for _ in range(height)]
        def p(node, i, l, r):
            if not node:
                return
            mid = l+r>>1
            res[i][mid] = str(node.val)
            p(node.left, i+1, l, mid)
            p(node.right, i+1, mid+1, r)
        p(root, 0, 0, 2**height-2)
        return res