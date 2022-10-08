# 题目：95.不同的二叉搜索树 II
# 难度：MEDIUM
# 最后提交：2022-06-24 17:07:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def p(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r+1):
                al = p(l, i-1)
                rl = p(i+1, r)
                for ln in al:
                    for rn in rl:
                        t = TreeNode(i)
                        t.left = ln
                        t.right = rn
                        res.append(t)
            return res
        return p(1, n)
        