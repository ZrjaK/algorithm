# 题目：1877.数组中最大数对和的最小值
# 难度：MEDIUM
# 最后提交：2022-03-31 21:44:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ma = -1e99
        for i in range(len(nums)//2):
            ma = max(ma, nums[i]+nums[-1-i])
        return ma

