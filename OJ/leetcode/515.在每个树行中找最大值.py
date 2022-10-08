# 题目：515.在每个树行中找最大值
# 难度：MEDIUM
# 最后提交：2022-04-14 04:53:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = [-1e99] * 10000
        def p(node, h):
            if not node:
                return
            res[h] = max(res[h], node.val)
            p(node.left, h+1)
            p(node.right, h+1)
        p(root, 0)
        return res[:res.index(-1e99)]