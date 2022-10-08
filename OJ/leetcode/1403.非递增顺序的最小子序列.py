# 题目：1403.非递增顺序的最小子序列
# 难度：EASY
# 最后提交：2022-03-25 20:22:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        nums.sort(reverse=True)
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            if t*2 > s:
                break
        return nums[:i+1]