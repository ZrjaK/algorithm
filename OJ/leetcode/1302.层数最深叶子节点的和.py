# 题目：1302.层数最深叶子节点的和
# 难度：MEDIUM
# 最后提交：2022-04-03 16:13:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = {}
        def p(node,h):
            if node == None:
                return
            if h in d.keys():
                d[h] += node.val
            else:
                d[h] = node.val
            p(node.left, h+1)
            p(node.right, h+1)


        p(root, 1)
        return d[max(d.keys())]