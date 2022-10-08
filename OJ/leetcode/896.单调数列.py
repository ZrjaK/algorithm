# 题目：896.单调数列
# 难度：EASY
# 最后提交：2021-11-01 22:32:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sorted(nums) == nums or sorted(nums) == nums[::-1]