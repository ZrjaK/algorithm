# 题目：107.二叉树的层序遍历 II
# 难度：MEDIUM
# 最后提交：2022-07-25 00:58:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur, nxt = 1, 0
        t = []
        q = deque([root])
        while q:
            node = q.popleft()
            t.append(node.val)
            cur -= 1
            if node.left:
                nxt += 1
                q.append(node.left)
            if node.right:
                nxt += 1
                q.append(node.right)
            if not cur:
                res.append(t)
                t = []
                cur = nxt
                nxt = 0
        return res[::-1]