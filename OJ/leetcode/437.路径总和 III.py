# 题目：437.路径总和 III
# 难度：MEDIUM
# 最后提交：2022-04-08 02:30:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def p(node):
            if not node:
                return []
            res = p(node.left) + p(node.right)
            for i in range(len(res)):
                res[i] += node.val
            res.append(node.val)
            self.ans += res.count(targetSum)
            return res
        p(root)
        return self.ans