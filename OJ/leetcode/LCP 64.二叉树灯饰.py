# 题目：LCP 64.二叉树灯饰
# 难度：MEDIUM
# 最后提交：2022-09-24 18:38:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

           
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def closeLampInTree(self, root: TreeNode) -> int:
        @cache
        def p(node, switchall, father_turned):
            status = node.val ^ father_turned
            res = 1e99
            for i in range(8):
                op1, op2, op3 = i>>2 & 1, i>>1 & 1, i & 1
                if ((status + op1 + op2 + op3) % 2) ^ switchall == 0:
                    t = op1 + op2 + op3
                    if node.left:
                        t += p(node.left, switchall ^ op2, op3)
                    if node.right:
                        t += p(node.right, switchall ^ op2, op3)
                    res = min(res, t)
            return res
        return p(root, 0, 0)