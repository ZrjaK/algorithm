# 题目：53.最大子数组和
# 难度：MEDIUM
# 最后提交：2022-09-07 15:19:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            ans = max(ans, nums[i])
        return ans