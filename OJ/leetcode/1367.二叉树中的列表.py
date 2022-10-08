# 题目：1367.二叉树中的列表
# 难度：MEDIUM
# 最后提交：2022-08-09 02:06:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        @cache
        def p(h, node):
            if not h:
                return True
            if not node:
                return False
            res = False
            if node.val == h.val:
                res |= p(h.next, node.left) or p(h.next, node.right)
            res |= p(head, node.left) or p(head, node.right)
            return res
        return p(head, root)