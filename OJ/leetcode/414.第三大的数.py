# 题目：414.第三大的数
# 难度：EASY
# 最后提交：2021-10-21 20:19:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=1)
        if len(nums) < 3:
            return nums[0]
        return nums[2]