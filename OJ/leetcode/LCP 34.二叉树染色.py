# 题目：LCP 34.二叉树染色
# 难度：MEDIUM
# 最后提交：2022-09-23 19:17:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        dp = defaultdict(lambda: [0] * (k+1))
        def p(node):
            if not node:
                return
            dp[node][1] = node.val
            p(node.left)
            p(node.right)
            dp[node][0] = max(dp[node.left]) + max(dp[node.right])
            for i in range(k, 0, -1):
                for j in range(i-1, -1, -1):
                    dp[node][i] = max(dp[node][i], node.val + dp[node.left][j] + dp[node.right][i-j-1])
        p(root)
        return max(dp[root])