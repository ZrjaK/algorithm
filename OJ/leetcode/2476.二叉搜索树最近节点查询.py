# 题目：2476.二叉搜索树最近节点查询
# 难度：MEDIUM
# 最后提交：2022-11-20 10:35:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        h = []
        def p(node):
            if not node:
                return
            h.append(node.val)
            p(node.left)
            p(node.right)
        p(root)
        h.sort()
        ans = []
        for i in queries:
            a = [-1, -1]
            t = bisect_right(h, i)
            if t:
                a[0] = h[t-1]
            t = bisect_left(h, i)
            if t < len(h):
                a[1] = h[t]
            ans.append(a)
        return ans