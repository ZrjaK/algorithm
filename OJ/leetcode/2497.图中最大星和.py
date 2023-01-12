# 题目：2497.图中最大星和
# 难度：MEDIUM
# 最后提交：2022-12-16 12:50:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = [[] for _ in vals]
        for x, y in edges:
            if vals[y] > 0: g[x].append(vals[y])
            if vals[x] > 0: g[y].append(vals[x])
        return max(v + sum(nlargest(k, a)) for v, a in zip(vals, g))
