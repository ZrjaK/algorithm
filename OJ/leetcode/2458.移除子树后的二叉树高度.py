# 题目：2458.移除子树后的二叉树高度
# 难度：HARD
# 最后提交：2022-10-30 12:55:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        dp = {}
        
        @cache
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        def dfs(root, cur, other):
            left, right = depth(root.left), depth(root.right)
            if root.left:
                dp[root.left.val] = max(cur+right+1, other)
                dfs(root.left, cur+1, dp[root.left.val])
            if root.right:
                dp[root.right.val] = max(cur+left+1, other)
                dfs(root.right, cur+1, dp[root.right.val] )   
        
        dfs(root, 0, 0)
        
        return [dp[q]-1 for q in queries]