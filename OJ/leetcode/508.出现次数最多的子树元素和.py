# 题目：508.出现次数最多的子树元素和
# 难度：MEDIUM
# 最后提交：2022-08-18 23:16:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        def p(node):
            if not node:
                return 0
            l = p(node.left)
            r = p(node.right)
            d[l+r+node.val] += 1
            return l+r+node.val
        p(root)
        res = []
        m = max(d.values())
        for i in d.keys():
            if d[i] == m:
                res.append(i)
        return res