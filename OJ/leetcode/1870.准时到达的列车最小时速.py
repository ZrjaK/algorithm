# 题目：1870.准时到达的列车最小时速
# 难度：MEDIUM
# 最后提交：2022-05-16 13:04:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n-1:
            return -1
        l, r = 1, int(1e7)
        ans = 0
        while l <= r:
            mid = l+r>>1
            s = 0
            for i in dist[:-1]:
                s += i // mid
                if i % mid != 0:
                    s += 1
            s += dist[-1]/mid
            if s <= hour:
                r = mid - 1
            else:
                l = mid + 1
        return l