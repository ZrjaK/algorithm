# 题目：998.最大二叉树 II
# 难度：MEDIUM
# 最后提交：2022-08-30 01:19:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def p(node):
            res = [node.val]
            if node.left:
                res = p(node.left) + res
            if node.right:
                res = res + p(node.right)
            return res
        h = p(root)
        h.append(val)
        def b(arr):
            if not arr:
                return None
            m = max(arr)
            i = arr.index(m)
            return TreeNode(m, left=b(arr[:i]), right=b(arr[i+1:]))
        return b(h)
