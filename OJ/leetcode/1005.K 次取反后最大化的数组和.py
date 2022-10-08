# 题目：1005.K 次取反后最大化的数组和
# 难度：EASY
# 最后提交：2021-11-03 19:30:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)
