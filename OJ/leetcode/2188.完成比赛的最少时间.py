# 题目：2188.完成比赛的最少时间
# 难度：HARD
# 最后提交：2022-09-28 14:05:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        min_sec = [inf] * 18
        for f, r in tires:
            x, time, sum = 1, f, 0
            while time <= changeTime + f:
                sum += time
                min_sec[x] = min(min_sec[x], sum)
                time *= r
                x += 1
        @cache
        def p(i):
            if i <= 0:
                return 0
            res = 1e99
            for j in range(1, 18):
                res = min(res, min_sec[j] + p(i-j))
            return res + changeTime
        return p(numLaps)-changeTime