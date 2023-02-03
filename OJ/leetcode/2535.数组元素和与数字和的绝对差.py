# 题目：2535.数组元素和与数字和的绝对差
# 难度：EASY
# 最后提交：2023-01-15 10:30:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for i in nums:
            for j in str(i):
                s2 += int(j)
        return abs(s1-s2)