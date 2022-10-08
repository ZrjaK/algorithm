# 题目：剑指 Offer II 055.二叉搜索树迭代器
# 难度：MEDIUM
# 最后提交：2022-10-07 11:52:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.h = []
        def p(node):
            if not node:
                return
            p(node.right)
            self.h.append(node.val)
            p(node.left)
        p(root)

    def next(self) -> int:
        return self.h.pop()

    def hasNext(self) -> bool:
        return self.h != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()