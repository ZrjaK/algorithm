# 题目：面试题 10.11.峰与谷
# 难度：MEDIUM
# 最后提交：2023-01-30 20:35:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2], nums[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]