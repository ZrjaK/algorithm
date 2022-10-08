# 题目：2406.将区间分为最少组数
# 难度：MEDIUM
# 最后提交：2022-09-11 10:39:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))
        pq = []
        for start, end in intervals:
            if not pq:
                heappush(pq, end)
                continue
            t = heappop(pq)
            if start > t:
                t = end
                heappush(pq, t)
            else:
                heappush(pq, t)
                heappush(pq, end)
        return len(pq)
        