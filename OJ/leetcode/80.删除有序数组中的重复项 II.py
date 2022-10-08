# 题目：80.删除有序数组中的重复项 II
# 难度：MEDIUM
# 最后提交：2022-05-26 13:35:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i