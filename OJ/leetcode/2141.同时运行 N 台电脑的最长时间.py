# 题目：2141.同时运行 N 台电脑的最长时间
# 难度：HARD
# 最后提交：2022-09-27 08:17:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        l, r = 0, 10**14
        while l <= r:
            mid = l+r>>1
            t = 0
            for b in batteries:
                t += min(b, mid)
            if t >= n * mid:
                l = mid + 1
            else:
                r = mid - 1
        return r