# 题目：222.完全二叉树的节点个数
# 难度：MEDIUM
# 最后提交：2022-08-18 16:32:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = root
        r = root
        count_l = 0
        count_r = 0
        while l:
            l = l.left
            count_l += 1
        while r:
            r = r.right
            count_r += 1
        if count_r == count_l:
            return pow(2,count_l)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)