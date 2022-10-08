# 题目：剑指 Offer II 054.所有大于等于节点的值之和
# 难度：MEDIUM
# 最后提交：2022-10-07 11:50:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def p(node, a):
            if not node:
                return 0
            r = p(node.right, a)
            l = p(node.left, a+node.val+r)
            t = l+r+node.val
            node.val = r+node.val+a
            return t
        p(root, 0)
        return root