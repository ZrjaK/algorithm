# 题目：652.寻找重复的子树
# 难度：MEDIUM
# 最后提交：2022-09-05 00:18:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if not node:
                return None
            uid = trees[node.val, lookup(node.left), lookup(node.right)]
            count[uid] += 1
            if count[uid] == 2:
                ans.append(node)
            return uid

        lookup(root)
        return ans