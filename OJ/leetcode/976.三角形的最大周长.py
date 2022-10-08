# 题目：976.三角形的最大周长
# 难度：EASY
# 最后提交：2021-11-03 13:10:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            a = nums[i]
            b = nums[i-1]
            c = nums[i-2]
            if b + c > a:
                return a + b + c
        return 0