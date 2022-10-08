# 题目：1749.任意子数组和的绝对值的最大值
# 难度：MEDIUM
# 最后提交：2022-07-20 01:01:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        h1 = [i for i in nums] + [0]
        for i in range(n):
            h1[i] = h1[i-1] + h1[i]
            if h1[i] < 0:
                h1[i] = 0
        h2 = [i for i in nums] + [0]
        for i in range(n):
            h2[i] = h2[i-1] + h2[i]
            if h2[i] > 0:
                h2[i] = 0
        return max(max(h1), -min(h2))