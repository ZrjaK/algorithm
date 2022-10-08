# 题目：剑指 Offer II 012.左右两边子数组的和相等
# 难度：EASY
# 最后提交：2022-10-04 16:26:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        h = list(accumulate(nums)) + [0]
        for i in range(n):
            if h[i-1] == h[-2] - h[i]:
                return i
        return -1