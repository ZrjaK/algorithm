# 题目：2154.将找到的值乘以 2
# 难度：EASY
# 最后提交：2022-04-21 11:32:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original