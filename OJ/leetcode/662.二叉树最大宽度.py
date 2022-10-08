# 题目：662.二叉树最大宽度
# 难度：MEDIUM
# 最后提交：2022-08-27 23:58:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        def p(node, i):
            if not node:
                return
            d[node] = i
            p(node.left, 2*i-1)
            p(node.right, 2*i)
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            t = []
            for _ in range(size):
                cur = q.popleft()
                if not cur:
                    continue
                t.append(cur)
                q.append(cur.left)
                q.append(cur.right)
            if t:
                res.append(t)
        p(root, 1)
        ans = 0
        for i in res:
            ans = max(ans, d[i[-1]]-d[i[0]])
        return ans + 1