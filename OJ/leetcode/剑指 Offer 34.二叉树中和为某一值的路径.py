# 题目：剑指 Offer 34.二叉树中和为某一值的路径
# 难度：MEDIUM
# 最后提交：2022-10-02 22:50:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res=  []
        def p(node, l):
            if not node:
                return
            if not node.left and not node.right:
                if sum(l)+node.val == target:
                    res.append(l+[node.val])
            p(node.left, l+[node.val])
            p(node.right, l+[node.val])
        p(root, [])
        return res