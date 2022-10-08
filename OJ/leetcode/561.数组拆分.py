# 题目：561.数组拆分
# 难度：EASY
# 最后提交：2021-10-22 19:21:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])