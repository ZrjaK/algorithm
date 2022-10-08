# 题目：783.二叉搜索树节点最小距离
# 难度：EASY
# 最后提交：2022-07-29 16:38:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        def p(node):
            if not node:
                return
            p(node.left)
            res.append(node.val)
            p(node.right)
        p(root)
        ans = 1e99
        for i in range(len(res)-1):
            ans = min(ans, abs(res[i]-res[i+1]))
        return ans