# 题目：1261.在受污染的二叉树中查找元素
# 难度：MEDIUM
# 最后提交：2022-08-06 18:19:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.s = set()
        def p(node, x):
            self.s.add(x)
            if node.left:
                p(node.left, 2*x+1)
            if node.right:
                p(node.right, 2*x+2)
        p(root, 0)
    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)