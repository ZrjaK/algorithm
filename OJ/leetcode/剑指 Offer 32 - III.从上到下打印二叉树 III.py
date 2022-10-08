# 题目：剑指 Offer 32 - III.从上到下打印二叉树 III
# 难度：MEDIUM
# 最后提交：2022-10-02 22:43:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        tmp = [root]
        c = 1
        while tmp:
            c ^= 1
            t = []
            n = len(tmp)
            for i in range(n):
                node = tmp[i]
                t.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            tmp = tmp[n:]
            res.append(t[::-1] if c else t)
        return res