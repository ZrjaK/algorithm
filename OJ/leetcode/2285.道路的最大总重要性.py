# 题目：2285.道路的最大总重要性
# 难度：MEDIUM
# 最后提交：2022-05-28 22:56:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(int)
        for i , j in roads:
            d[i] += 1
            d[j] += 1
        pq = []
        for i, j in d.items():
            heapq.heappush(pq, (-j, i))
        h = [0] * n
        c = n
        while pq:
            t = heapq.heappop(pq)
            h[t[1]] = c
            c -= 1
        # print(h)
        ans = 0
        for i, j in roads:
            ans += h[i] + h[j]
        return ans