# 题目：2415.反转二叉树的奇数层
# 难度：MEDIUM
# 最后提交：2022-09-18 10:44:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        for i in range(len(res)):
            if i % 2:
                res[i] = res[i][::-1]
        def build(i, j):
            if i == len(res):
                return None
            node = TreeNode(res[i][j])
            node.left = build(i+1, 2*j)
            node.right = build(i+1, 2*j+1)
            return node
        return build(0, 0)