# 题目：114.二叉树展开为链表
# 难度：MEDIUM
# 最后提交：2022-08-18 16:17:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def p(node):
            if not node:
                return
            res.append(node)
            p(node.left)
            p(node.right)
        p(root)
        for i in range(len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        if res:
            res[-1].left = None
            res[-1].right = None