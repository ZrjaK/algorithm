# 题目：1606.找到处理最多请求的服务器
# 难度：HARD
# 最后提交：2022-09-27 09:18:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        s = SortedList(list(range(k)))
        n = len(arrival)
        pq = []
        ans = [0] * k
        for i in range(n):
            while pq and pq[0][0] <= arrival[i]:
                s.add(heappop(pq)[1])
            t = s.bisect_left(i%k)
            if t == len(s):
                t = 0
            if s:
                heappush(pq, [arrival[i]+load[i], s[t]])
                ans[s[t]] += 1
                s.pop(t)
        ma = max(ans)
        return [i for i in range(k) if ans[i] == ma]