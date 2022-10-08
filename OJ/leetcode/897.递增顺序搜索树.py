# 题目：897.递增顺序搜索树
# 难度：EASY
# 最后提交：2022-08-18 01:21:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def p(node):
            if not node:
                return
            p(node.left)
            res.append(node)
            p(node.right)
        p(root)
        if not res:
            return None
        root = res[0]
        for i in range(len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        res[-1].left = None
        res[-1].right = None
        return root