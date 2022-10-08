# 题目：435.无重叠区间
# 难度：MEDIUM
# 最后提交：2022-04-08 02:03:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x: x[0])
        end = intervals[0][1]
        ans = -1
        for i in intervals:
            if i[0] < end:
                ans += 1
                end = min(end, i[1])
            else:
                end = i[1]
        return ans