# 题目：581.最短无序连续子数组
# 难度：MEDIUM
# 最后提交：2022-10-03 14:41:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        h = sorted(nums)
        n = len(nums)
        l, r = 0, n-1
        while l < n and nums[l] == h[l]:
            l += 1
        while r >= 0 and nums[r] == h[r]:
            r -= 1
        return max(0, r-l+1)