# 题目：99.恢复二叉搜索树
# 难度：MEDIUM
# 最后提交：2022-08-18 01:50:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p = lambda x: p(x.left) + [x] + p(x.right) if x else []
        a = p(root)
        sa = sorted(a, key=lambda x: x.val)
        p, q = [a[i] for i in range(len(a)) if a[i] != sa[i]]
        p.val, q.val = q.val, p.val