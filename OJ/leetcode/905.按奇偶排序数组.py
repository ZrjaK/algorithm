# 题目：905.按奇偶排序数组
# 难度：EASY
# 最后提交：2021-11-01 22:42:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums