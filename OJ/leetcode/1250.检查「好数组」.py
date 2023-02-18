# 题目：1250.检查「好数组」
# 难度：HARD
# 最后提交：2023-02-15 12:41:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1