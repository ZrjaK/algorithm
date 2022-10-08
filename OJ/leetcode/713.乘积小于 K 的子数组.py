# 题目：713.乘积小于 K 的子数组
# 难度：MEDIUM
# 最后提交：2022-05-05 00:34:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        n = len(nums)
        l = r = ans = 0
        c = 1
        while r < n:
            c *= nums[r]
            while not c < k:
                c //= nums[l]
                l += 1
            ans += r-l+1
            r += 1
        return ans