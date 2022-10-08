# 题目：436.寻找右区间
# 难度：MEDIUM
# 最后提交：2022-04-25 06:27:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        h = [(i, intervals[i][0], intervals[i][1]) for i in range(n)]
        h.sort(key=lambda x:x[2])
        h.sort(key=lambda x:x[1])
        s = [i[1] for i in h]
        res = []
        for start, end in intervals:
            t = bisect_left(s, end)
            if t < n:
                res.append(h[t][0])
            else:
                res.append(-1)
        return res