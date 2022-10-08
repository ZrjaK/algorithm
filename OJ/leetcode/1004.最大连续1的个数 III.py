# 题目：1004.最大连续1的个数 III
# 难度：MEDIUM
# 最后提交：2022-05-22 07:58:50 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = c = 0
        for r in range(len(nums)):
            c += nums[r]
            if c + k < r - l + 1:
                c -= nums[l]
                l += 1
        return len(nums) - l
            
