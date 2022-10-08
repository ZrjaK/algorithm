# 题目：337.打家劫舍 III
# 难度：MEDIUM
# 最后提交：2022-09-23 19:01:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(lambda: [0] * 2)
        def p(node):
            if not node:
                return
            dp[node][1] = node.val
            p(node.left)
            p(node.right)
            dp[node][1] += dp[node.left][0] + dp[node.right][0]
            dp[node][0] += max(dp[node.left]) + max(dp[node.right])
        p(root)
        return max(dp[root])