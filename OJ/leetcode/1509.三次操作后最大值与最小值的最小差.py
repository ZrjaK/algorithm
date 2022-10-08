# 题目：1509.三次操作后最大值与最小值的最小差
# 难度：MEDIUM
# 最后提交：2022-08-31 14:46:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[i-4]-nums[i] for i in range(4))