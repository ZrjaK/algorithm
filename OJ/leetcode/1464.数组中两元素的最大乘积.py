# 题目：1464.数组中两元素的最大乘积
# 难度：EASY
# 最后提交：2022-08-26 23:01:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)