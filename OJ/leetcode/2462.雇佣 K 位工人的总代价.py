# 题目：2462.雇佣 K 位工人的总代价
# 难度：MEDIUM
# 最后提交：2022-11-06 10:42:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = deque([[v, i] for i, v in enumerate(costs)])
        pq = []
        for _ in range(candidates):
            heappush(pq, q.pop()+[1])
        for _ in range(candidates):
            if q:
                heappush(pq, q.popleft()+[0])
        ans = 0
        for _ in range(k):
            t = heappop(pq)
            ans += t[0]
            if t[2] == 1:
                if q:
                    heappush(pq, q.pop()+[1])
            else:
                if q:
                    heappush(pq, q.popleft()+[0])
        return ans