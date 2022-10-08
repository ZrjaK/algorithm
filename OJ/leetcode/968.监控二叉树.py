# 题目：968.监控二叉树
# 难度：HARD
# 最后提交：2022-04-08 18:32:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        @lru_cache(None)
        def p(node):
            if not node:
                return [1e99, 0, 1e99] 
            # [不被监控不放相机，被监控不放相机，被监控放相机]
            p0 = p(node.left)[1] + p(node.right)[1]
            p1 = min(p(node.left)[2] + p(node.right)[2], 
                    p(node.left)[1] + p(node.right)[2],
                    p(node.left)[2] + p(node.right)[1])
            p2 = 1 + min(p(node.left)) + min(p(node.right))
            return [p0,p1,p2]
        t = p(root)
        return min(t[0]+1, t[1], t[2])