# 题目：857.雇佣 K 名工人的最低成本
# 难度：HARD
# 最后提交：2022-09-11 00:26:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        h = sorted(list(zip(quality, wage)), key=lambda x: -x[0]/x[1])
        pq = []
        ans = 1e99
        tq = 0
        for q, w in h[:k-1]:
            tq += q
            heappush(pq, -q)
        for q, w in h[k-1:]:
            tq += q
            heappush(pq, -q)
            ans = min(ans, w * tq / q)
            tq += heappop(pq)
        return ans