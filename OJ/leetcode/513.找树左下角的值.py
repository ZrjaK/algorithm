# 题目：513.找树左下角的值
# 难度：MEDIUM
# 最后提交：2022-04-14 04:27:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        while queue:
            root = queue.popleft()
            if root.right:
                queue.append(root.right)
            if root.left:
                queue.append(root.left)
        return root.val
