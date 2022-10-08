# 题目：1305.两棵二叉搜索树中的所有元素
# 难度：MEDIUM
# 最后提交：2022-04-03 16:28:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        r1, r2 = [], []
        def p1(node):
            if node == None:
                return
            p1(node.left)
            r1.append(node.val)
            p1(node.right)
        def p2(node):
            if node == None:
                return
            p2(node.left)
            r2.append(node.val)
            p2(node.right)
        p1(root1);p2(root2)
        p1 = p2 = 0
        r = []
        while p1 < len(r1) and p2 < len(r2):
            if r1[p1] < r2[p2]:
                r.append(r1[p1])
                p1 += 1
            else:
                r.append(r2[p2])
                p2 += 1
        r += r1[p1:]+r2[p2:]
        return r