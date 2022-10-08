# 题目：1379.找出克隆二叉树中的相同节点
# 难度：MEDIUM
# 最后提交：2022-08-09 02:14:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def p(node):
            if not node:
                return None
            if node.val == target.val:
                return node
            res = p(node.left)
            if res:
                return res
            res = p(node.right)
            if res:
                return res
            return None
        return p(cloned)