# 题目：971.翻转二叉树以匹配先序遍历
# 难度：MEDIUM
# 最后提交：2022-08-19 17:22:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        res = []
        i = 0
        def dfs(node):
            nonlocal i
            nonlocal res
            if node:
                if node.val != voyage[i]:
                    res = [-1]
                    return
                i += 1
                if i < len(voyage) and node.left and node.left.val != voyage[i]:
                    res.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        if res and res[0] == -1:
            res = [-1]
        return res
                