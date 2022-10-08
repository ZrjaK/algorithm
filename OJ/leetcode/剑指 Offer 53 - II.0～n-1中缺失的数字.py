# 题目：剑指 Offer 53 - II.0～n-1中缺失的数字
# 难度：EASY
# 最后提交：2022-10-03 19:00:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        v = set(nums)
        for i in range(n+1):
            if i not in v:
                return i