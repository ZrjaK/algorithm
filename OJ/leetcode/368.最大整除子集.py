# 题目：368.最大整除子集
# 难度：MEDIUM
# 最后提交：2022-06-29 19:43:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        if len(nums) == 1: return nums
        l = len(nums)
        nums.sort()

        dp = [[i] for i in nums]
        
        for i in range(1, l):
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i],key=len)

        return max(dp,key=len)