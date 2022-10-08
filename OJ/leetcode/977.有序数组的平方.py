# 题目：977.有序数组的平方
# 难度：EASY
# 最后提交：2021-11-03 13:13:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i ** 2 for i in nums])