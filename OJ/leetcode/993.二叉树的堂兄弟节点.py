# 题目：993.二叉树的堂兄弟节点
# 难度：EASY
# 最后提交：2022-07-29 17:06:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            t = []
            for _ in range(size):
                cur = q.popleft()
                if not cur:
                    t.append(1e99)
                    continue
                t.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if t:
                res.append(t)
        # print(res)
        for i in res:
            if x in i and y in i and (abs(i.index(x)-i.index(y)) != 1 or min(i.index(x) ,i.index(y)) % 2 == 1):
                return True
        return False