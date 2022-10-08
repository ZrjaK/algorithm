# 题目：413.等差数列划分
# 难度：MEDIUM
# 最后提交：2022-07-05 00:55:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        dp = ans = 0
        d1 = nums[1] - nums[0]
        for i in range(2, len(nums)):
            d2 = nums[i] - nums[i-1]
            if d2 == d1:
                dp += 1
                ans += dp
            else:
                dp = 0
            d1 = d2
        return ans