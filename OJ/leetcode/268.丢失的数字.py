# 题目：268.丢失的数字
# 难度：EASY
# 最后提交：2021-10-21 16:54:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)