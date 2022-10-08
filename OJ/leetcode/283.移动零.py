# 题目：283.移动零
# 难度：EASY
# 最后提交：2021-10-21 17:25:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)