# 题目：1028.从先序遍历还原二叉树
# 难度：HARD
# 最后提交：2022-12-11 19:33:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        q = [TreeNode()]
        c = 0
        d = {q[0]: -1}
        i = 0
        while i < n:
            if traversal[i] == "-":
                c += 1
                i += 1
            else:
                j = i
                while j < n:
                    if traversal[j] == "-":
                        break
                    j += 1
                t = TreeNode(int(traversal[i:j]))
                d[t] = c
                while d[q[-1]] >= c:
                    q.pop()
                if d[q[-1]] == c - 1:
                    if not q[-1].left:
                        q[-1].left = t
                    else:
                        q[-1].right = t
                q.append(t)
                c = 0
                i = j
        return q[0].left
                