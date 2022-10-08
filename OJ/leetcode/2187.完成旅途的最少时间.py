# 题目：2187.完成旅途的最少时间
# 难度：MEDIUM
# 最后提交：2022-05-19 09:30:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l ,r = min(time), max(time) * totalTrips
        ans = 0
        while l <= r:
            mid = l+r>>1
            s = 0
            for i in time:
                s += mid // i
            if s < totalTrips:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans