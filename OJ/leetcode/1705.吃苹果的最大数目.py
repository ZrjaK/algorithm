# 题目：1705.吃苹果的最大数目
# 难度：MEDIUM
# 最后提交：2022-09-07 13:23:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        n = len(apples)
        pq = []
        i = 0
        while pq or i < n:
            if i < n:
                heappush(pq, [i+days[i], apples[i]])
            while pq and (pq[0][0] <= i or not pq[0][1]):
                heappop(pq)
            if pq:
                t = heappop(pq)
                t[1] -= 1
                heappush(pq, t)
                ans += 1
            i += 1
        return ans