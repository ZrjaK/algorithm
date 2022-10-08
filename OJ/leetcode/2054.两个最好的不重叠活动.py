# 题目：2054.两个最好的不重叠活动
# 难度：MEDIUM
# 最后提交：2022-07-23 01:17:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[0])
        ans = 0
        pq = []
        ma = 0
        for start, end, score in events:
            while pq and pq[0][0] < start:
                ma = max(ma, heapq.heappop(pq)[1])
            ans = max(ans, ma + score)
            heapq.heappush(pq, (end, score))
        return ans