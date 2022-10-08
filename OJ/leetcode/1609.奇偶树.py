# 题目：1609.奇偶树
# 难度：MEDIUM
# 最后提交：2022-08-10 21:24:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = float('inf') if level % 2 else 0
            nxt = []
            for node in queue:
                val = node.val
                if val % 2 == level % 2 or level % 2 == 0 and val <= prev or level % 2 == 1 and val >= prev:
                    return False
                prev = val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            level += 1
        return True