# 题目：2385.感染二叉树需要的总时间
# 难度：MEDIUM
# 最后提交：2022-08-21 10:43:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d = defaultdict(list)
        def p(node):
            if not node:
                return
            if node.left:
                d[node.val].append(node.left.val)
                d[node.left.val].append(node.val)
            if node.right:
                d[node.val].append(node.right.val)
                d[node.right.val].append(node.val)
            p(node.left)
            p(node.right)
        p(root)
        q = deque([(0,start)])
        ans = 0
        v = set()
        while q:
            s, t = q.popleft()
            if t in v:
                continue
            v.add(t)
            ans = max(ans, s)
            for nxt in d[t]:
                q.append((s+1, nxt))
        return ans