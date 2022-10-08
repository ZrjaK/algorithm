# 题目：2374.边积分最高的节点
# 难度：MEDIUM
# 最后提交：2022-08-14 10:35:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        h = [0] * n
        for i in range(n):
            h[edges[i]] += i
        return h.index(max(h))