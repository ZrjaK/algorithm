# 题目：502.IPO
# 难度：HARD
# 最后提交：2022-04-20 18:28:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        n = len(profits)
        a = [[p,c] for p,c in zip(profits, capital)]
        a.sort(key=lambda x:x[1],reverse=True)
        pq = []
        for _ in range(k):
            while a and a[-1][1] <= w:
                heapq.heappush(pq,-a.pop()[0])
            if not pq:
                break
            w += -heapq.heappop(pq)
        return w
