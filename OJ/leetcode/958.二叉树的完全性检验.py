# 题目：958.二叉树的完全性检验
# 难度：MEDIUM
# 最后提交：2022-08-03 23:19:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            t = []
            for _ in range(size):
                cur = q.popleft()
                if not cur:
                    t.append(0)
                    continue
                t.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if t:
                res.append(t)
        res.pop()
        for i in res[:-1]:
            if 0 in i:
                return False
        flag = False
        for i in res[-1][::-1]:
            if i:
                flag = True
            elif flag:
                return False
        return True