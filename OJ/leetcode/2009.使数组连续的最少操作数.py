# 题目：2009.使数组连续的最少操作数
# 难度：HARD
# 最后提交：2022-09-19 08:26:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = n-1
        for i in range(len(nums)):
            t = bisect_left(nums, nums[i]-n+1)
            ans = min(ans, n-1-(i-t))
        return ans