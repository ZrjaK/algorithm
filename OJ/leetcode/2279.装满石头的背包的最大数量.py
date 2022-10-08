# 题目：2279.装满石头的背包的最大数量
# 难度：MEDIUM
# 最后提交：2022-05-22 10:37:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        pq = []
        for i, j in zip(capacity, rocks):
            heapq.heappush(pq, (i-j))
        ans = 0
        while pq and additionalRocks > 0:
            t = heapq.heappop(pq)
            additionalRocks -= t
            ans += 1
        if additionalRocks < 0:
            ans -= 1
        return ans