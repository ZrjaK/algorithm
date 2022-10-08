# 题目：628.三个数的最大乘积
# 难度：EASY
# 最后提交：2021-10-23 10:51:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
        