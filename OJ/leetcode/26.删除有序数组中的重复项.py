# 题目：26.删除有序数组中的重复项
# 难度：EASY
# 最后提交：2021-10-20 14:28:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)-1, i,-1):
                if nums[i] == nums[j]:
                    del nums[j]
        return len(nums)