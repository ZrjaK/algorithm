# 题目：915.分割数组
# 难度：MEDIUM
# 最后提交：2022-10-24 00:32:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        s = SortedList(nums)
        ma = -1e99
        for i in nums:
            s.remove(i)
            ma = max(ma, i)
            if ma <= s[0]:
                return len(nums) - len(s)