# 题目：645.错误的集合
# 难度：EASY
# 最后提交：2021-10-23 11:21:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]