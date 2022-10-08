# 题目：剑指 Offer 03.数组中重复的数字
# 难度：EASY
# 最后提交：2022-09-30 10:51:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in sorted(c, key=lambda x: c[x], reverse=True):
            return i