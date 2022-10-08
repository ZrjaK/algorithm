# 题目：1022.从根到叶的二进制数之和
# 难度：EASY
# 最后提交：2022-08-18 01:29:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def p(node, l):
            if not node:
                return
            if not node.left and not node.right:
                l = l + [node.val]
                s = 0
                l = l[::-1]
                for i in range(len(l)):
                    if l[i]:
                        s += 1<<i
                res[0] += s
            p(node.left, l + [node.val])
            p(node.right, l + [node.val])
        p(root, [])
        return res[0]