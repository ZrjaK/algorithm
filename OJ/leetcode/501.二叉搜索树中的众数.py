# 题目：501.二叉搜索树中的众数
# 难度：EASY
# 最后提交：2022-08-18 00:55:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        def p(node):
            if not node:
                return
            d[node.val] += 1
            p(node.left)
            p(node.right)
        p(root)
        return [i for i in d.keys() if d[i] == max(d.values())]