# 题目：961.在长度 2N 的数组中找出重复 N 次的元素
# 难度：EASY
# 最后提交：2021-11-03 12:55:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] == nums[1]:
            return nums[0]
        else:
            return nums[len(nums) // 2]