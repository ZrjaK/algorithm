# 题目：剑指 Offer 32 - II.从上到下打印二叉树 II
# 难度：EASY
# 最后提交：2022-10-02 22:41:58 +0800 CST
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
        while tmp:
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
            res.append(t)
        return res