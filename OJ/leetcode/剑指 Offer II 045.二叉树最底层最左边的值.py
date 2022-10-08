# 题目：剑指 Offer II 045.二叉树最底层最左边的值
# 难度：MEDIUM
# 最后提交：2022-10-06 21:23:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
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
                t.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if t:
                res.append(t)
        return res[-1][0]