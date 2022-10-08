# 题目：228.汇总区间
# 难度：EASY
# 最后提交：2021-10-21 12:17:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        li = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[i] + j - i:
                j += 1
            li.append(str(nums[i]) if i == j - 1 else str(nums[i]) + '->' + str(nums[j - 1]))
            i = j
        return li