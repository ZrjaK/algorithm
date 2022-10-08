# 题目：894.所有可能的真二叉树
# 难度：MEDIUM
# 最后提交：2022-07-08 15:37:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        @cache
        def p(i):
            if i == 1:
                return [TreeNode(0)]
            res = []
            for j in range(1, i-1, 2):
                left = p(j)
                right = p(i-1-j)
                for l in left:
                    for r in right:
                        h = TreeNode(0, l, r)
                        res.append(h)
            return res
        return p(n)


