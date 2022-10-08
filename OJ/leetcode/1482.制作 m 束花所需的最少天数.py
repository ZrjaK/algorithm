# 题目：1482.制作 m 束花所需的最少天数
# 难度：MEDIUM
# 最后提交：2022-05-06 01:23:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l, r = 1, max(bloomDay)
        while l <= r:
            mid = l+r>>1
            b = [i for i in bloomDay]
            for i in range(len(b)):
                b[i] -= mid
            t = 0
            f = 0
            for i in b:
                if i <= 0:
                    t += 1
                else:
                    t = 0
                if t == k:
                    f += 1
                    t = 0
            if f >= m:
                r = mid - 1
            else:
                l = mid + 1
        return l