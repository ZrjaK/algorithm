# 题目：113.路径总和 II
# 难度：MEDIUM
# 最后提交：2022-08-18 01:52:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=  []
        def p(node, l):
            if not node:
                return
            if not node.left and not node.right:
                if sum(l)+node.val == targetSum:
                    res.append(l+[node.val])
            p(node.left, l+[node.val])
            p(node.right, l+[node.val])
        p(root, [])
        return res