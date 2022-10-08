# 题目：136.只出现一次的数字
# 难度：EASY
# 最后提交：2021-10-20 22:38:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a