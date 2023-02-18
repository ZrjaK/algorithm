# 题目：2558.从数量最多的堆取走礼物
# 难度：EASY
# 最后提交：2023-02-05 10:32:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = [-i for i in gifts]
        heapify(pq)
        for _ in range(k):
            t = -heappop(pq)
            t = int(t**0.5)
            heappush(pq, -t)
        return -sum(pq)