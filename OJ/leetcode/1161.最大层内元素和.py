# 题目：1161.最大层内元素和
# 难度：MEDIUM
# 最后提交：2022-08-06 02:01:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
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
        h = [sum(i) for i in res]
        return h.index(max(h)) + 1