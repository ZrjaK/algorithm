# 题目：2563.统计公平数对的数目
# 难度：MEDIUM
# 最后提交：2023-02-12 10:34:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()
        ans = 0
        for i in nums:
            ans += sl.bisect_right(upper - i) - sl.bisect_left(lower - i)
            sl.add(i)
        return ans