# 题目：1395.统计作战单位数
# 难度：MEDIUM
# 最后提交：2022-07-15 16:23:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        s = SortedList()
        l = []
        for i in rating:
            l.append(s.bisect_left(i))
            s.add(i)
        r = []
        s.clear()
        for i in rating[::-1]:
            r.append(s.bisect_left(i))
            s.add(i)
        r = r[::-1]
        ans = 0
        for i in range(n):
            ans += l[i] * (n-i-1-r[i]) + (i-l[i]) * r[i]
        return ans
