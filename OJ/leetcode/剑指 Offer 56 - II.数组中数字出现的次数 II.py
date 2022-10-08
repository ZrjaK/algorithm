# 题目：剑指 Offer 56 - II.数组中数字出现的次数 II
# 难度：MEDIUM
# 最后提交：2022-10-03 20:19:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in nums:
            if c[i] == 1:
                return i