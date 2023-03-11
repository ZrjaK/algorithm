# 题目：1326.灌溉花园的最少水龙头数目
# 难度：HARD
# 最后提交：2023-02-21 10:27:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rightMost = list(range(n + 1))
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            rightMost[start] = max(rightMost[start], end)

        last = ret = pre = 0
        for i in range(n):
            last = max(last, rightMost[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        return ret
