# 题目：453.最小操作次数使数组元素相等
# 难度：MEDIUM
# 最后提交：2021-10-22 00:37:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)