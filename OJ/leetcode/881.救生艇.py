# 题目：881.救生艇
# 难度：MEDIUM
# 最后提交：2022-06-06 19:13:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s = SortedList(people)
        ans = 0
        while s:
            k = s[-1]
            s.remove(k)
            t = s.bisect_right(limit-k)
            if s and t > 0 and s[t-1] + k <= limit:
                s.pop(t-1)
            ans += 1
        return ans