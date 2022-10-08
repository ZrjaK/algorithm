# 题目：1288.删除被覆盖区间
# 难度：MEDIUM
# 最后提交：2022-08-30 15:12:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        l = r = -1
        ans = 0
        for i, j in intervals:
            if i >= l and j <= r:
                continue
            else:
                ans += 1
                l, r = i, j
        return ans