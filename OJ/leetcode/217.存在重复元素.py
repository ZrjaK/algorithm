# 题目：217.存在重复元素
# 难度：EASY
# 最后提交：2021-10-21 11:24:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))