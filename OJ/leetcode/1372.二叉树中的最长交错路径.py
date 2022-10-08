# 题目：1372.二叉树中的最长交错路径
# 难度：MEDIUM
# 最后提交：2022-07-15 15:34:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        ans = [0]
        def p(node):
            if node == None:
                return [0, 0]
            res1 = p(node.left)
            res2 = p(node.right)
            ans[0] = max(ans[0], res1[1]+1, res2[0]+1)
            return [res1[1]+1, res2[0]+1]
        p(root)
        return ans[0]-1


            