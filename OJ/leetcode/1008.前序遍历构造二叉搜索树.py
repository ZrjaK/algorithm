# 题目：1008.前序遍历构造二叉搜索树
# 难度：MEDIUM
# 最后提交：2022-09-03 14:12:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(preorder[0])
        stack = [head]
        for i in preorder[1:]:
            if stack[-1].val > i:
                node = TreeNode(i)
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < i:
                    t = stack.pop()
                node = TreeNode(i)
                t.right = node
                stack.append(node)
        return head