# 题目：2265.统计值等于子树平均值的节点数
# 难度：MEDIUM
# 最后提交：2022-05-08 10:40:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = []
        def p(node):
            if not node:
                return [0, 0]
            p1 = p(node.left)
            p2 = p(node.right)
            res = p1[0] + p2[0] + node.val
            count = p1[1]+p2[1]+1
            if node.val == res // count:
                ans.append(node)
            return [res, count]
        p(root)
        return len(ans)