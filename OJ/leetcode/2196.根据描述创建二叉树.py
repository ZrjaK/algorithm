# 题目：2196.根据描述创建二叉树
# 难度：MEDIUM
# 最后提交：2022-08-13 17:07:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = defaultdict(TreeNode)
        v1 = set()
        v2 = set()
        for p, c, l in descriptions:
            d[p].val = p
            d[c].val = c
            if l:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
            v1.add(p)
            v2.add(c)
        for i in v1:
            if i not in v2:
                return d[i]