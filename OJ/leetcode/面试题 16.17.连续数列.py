# 题目：面试题 16.17.连续数列
# 难度：EASY
# 最后提交：2023-01-03 01:27:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)