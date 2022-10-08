# 题目：剑指 Offer 68 - II.二叉树的最近公共祖先
# 难度：EASY
# 最后提交：2022-10-03 22:26:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = {}
        parent = {}
        def dfs(node):
            if not node:
                return
            d[node.val] = node
            if node.left:
                parent[node.left.val] = node.val
                dfs(node.left)
            if node.right:
                parent[node.right.val] = node.val
                dfs(node.right)
        dfs(root)
        dp = defaultdict(lambda: [-1e99] * 32)
        for i in d:
            if i in parent:
                dp[i][0] = parent[i]
        for j in range(1, 32):
            for i in d:
                if dp[i][j-1] != -1e99:
                    dp[i][j] = dp[dp[i][j-1]][j-1]
        d1 = 0
        x = p.val
        while x != root.val:
            for j in range(31, -1, -1):
                if dp[x][j] != -1e99:
                    d1 += 2 ** j
                    x = dp[x][j]
                    break
        d2 = 0
        x = q.val
        while x != root.val:
            for j in range(31, -1, -1):
                if dp[x][j] != -1e99:
                    d2 += 2 ** j
                    x = dp[x][j]
                    break
        x, y = p.val, q.val
        if d1 > d2:
            x, y = y, x
            d1, d2 = d2, d1
        c = d2 - d1
        while c:
            f = c & -c
            j = -1
            while f:
                f >>= 1
                j += 1
            y = dp[y][j]
            c = c & c-1
        while x != y:
            for j in range(32):
                if dp[x][j] != -1e99 and dp[y][j] != -1e99:
                    x = dp[x][j]
                    y = dp[y][j]
                    break
        return d[x]