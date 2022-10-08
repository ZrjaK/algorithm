# 题目：133.克隆图
# 难度：MEDIUM
# 最后提交：2022-07-26 17:55:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        res = Node(node.val)
        visited = set()
        q = deque([[res, node]])
        d = {1:res}
        while q:
            nd, node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for n in node.neighbors:
                if n.val in d:
                    t = d[n.val]
                else:
                    t = Node(n.val)
                    d[n.val] = t
                q.append([t, n])
                nd.neighbors.append(t)
        return res