# 题目：剑指 Offer II 009.乘积小于 K 的子数组
# 难度：MEDIUM
# 最后提交：2022-10-04 16:15:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        s = 1
        for r in range(len(nums)):
            s *= nums[r]
            while l < r and s >= k:
                s //= nums[l]
                l += 1
            if s < k:
                ans += r-l+1
        return ans