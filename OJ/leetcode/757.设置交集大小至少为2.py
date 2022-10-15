# 题目：757.设置交集大小至少为2
# 难度：HARD
# 最后提交：2022-10-11 21:27:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))
        a, b, ans = -1, -1, 0
        for l, r in intervals:
            if l > b:
                a, b = r - 1, r
                ans += 2
            elif l > a:
                a, b, = b, r
                ans += 1
        return ans