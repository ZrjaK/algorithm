# 题目：1838.最高频元素的频数
# 难度：MEDIUM
# 最后提交：2022-05-24 23:04:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l = s = 0
        for r in range(n):
            s += nums[r]
            t = nums[r] * (r-l+1)
            if s + k < t:
                s -= nums[l]
                l += 1
        return n-l