# 题目：1722.执行交换操作后的最小汉明距离
# 难度：MEDIUM
# 最后提交：2022-08-17 22:15:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        for i, j in allowedSwaps:
            union(i, j)
        d = defaultdict(dict)
        for i in range(n):
            if source[i] in d[find(i)]:
                d[find(i)][source[i]] += 1
            else:
                d[find(i)][source[i]] = 1
        ans = 0
        for i in range(n):
            if target[i] in d[find(i)] and d[find(i)][target[i]] > 0:
                d[find(i)][target[i]] -= 1
            else:
                ans += 1
        return ans