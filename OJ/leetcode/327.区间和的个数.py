# 题目：327.区间和的个数
# 难度：HARD
# 最后提交：2022-08-24 14:40:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        s = SortedList([0])
        ans = 0
        for i in accumulate(nums):
            ans += s.bisect_right(i-lower) - s.bisect_left(i-upper)
            s.add(i)
        return ans
