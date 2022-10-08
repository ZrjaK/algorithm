# 题目：剑指 Offer 42.连续子数组的最大和
# 难度：EASY
# 最后提交：2022-10-03 11:27:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)