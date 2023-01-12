# 题目：2528.最大化城市的最小供电站数目
# 难度：HARD
# 最后提交：2023-01-07 23:08:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 2*r + 10)
        for i in range(n):
            diff[i-r] += stations[i]
            diff[i+r+1] -= stations[i]
        s = 0
        h = []
        for i in range(-r, n):
            s += diff[i]
            if i >= 0:
                h.append(s)
        def check(x):
            diff = [0] * (n + 2*r + 10)
            s = 0
            res = 0
            for i in range(n):
                s += diff[i]
                if h[i] + s < x:
                    t = x - (h[i] + s)
                    diff[i+2*r+1] -= t
                    res += t
                    s += t
            return res <= k
        L, R = -1, 1<<60
        while L + 1 < R:
            mid = L + R >> 1
            if check(mid):
                L = mid
            else:
                R = mid
                
        return L