# 题目：1353.最多可以参加的会议数目
# 难度：MEDIUM
# 最后提交：2022-09-07 08:44:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0], reverse=True)
        pq = []
        t = 0
        ans = 0
        while pq or events:
            while events and events[-1][0] == t:
                heappush(pq, events.pop()[1])
            while pq and pq[0] < t:
                heappop(pq)
            if pq:
                heappop(pq)
                ans += 1
            t += 1
        return ans
