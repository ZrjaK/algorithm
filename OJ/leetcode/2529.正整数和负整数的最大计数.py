# 题目：2529.正整数和负整数的最大计数
# 难度：EASY
# 最后提交：2023-01-08 15:27:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len([i for i in nums if i > 0]), len([i for i in nums if i < 0]))