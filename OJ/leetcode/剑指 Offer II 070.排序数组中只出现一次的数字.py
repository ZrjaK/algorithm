# 题目：剑指 Offer II 070.排序数组中只出现一次的数字
# 难度：MEDIUM
# 最后提交：2022-10-08 12:39:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(xor, nums)