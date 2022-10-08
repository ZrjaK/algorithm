# 题目：1448.统计二叉树中好节点的数目
# 难度：MEDIUM
# 最后提交：2022-08-10 18:13:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def p(node, v):
            if not node:
                return
            if node.val >= v:
                res[0] += 1
            p(node.left, max(node.val, v))
            p(node.right, max(node.val, v))
        p(root, root.val)
        return res[0]