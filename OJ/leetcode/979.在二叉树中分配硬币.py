# 题目：979.在二叉树中分配硬币
# 难度：MEDIUM
# 最后提交：2022-08-19 17:35:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def p(node):
            nonlocal res
            if not node:
                return [0, 0]
            r1 = p(node.left)
            r2 = p(node.right)
            res += abs(r1[1]+r2[1]+node.val - (r1[0]+r2[0]+1))
            return [r1[0]+r2[0]+1, r1[1]+r2[1]+node.val]
        p(root)
        return res