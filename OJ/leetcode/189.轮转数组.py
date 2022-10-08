# 题目：189.轮转数组
# 难度：MEDIUM
# 最后提交：2022-06-01 18:11:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def p(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        if n < 2:
            return
        k %= n
        p(0, n-1)
        p(0, k-1)
        p(k, n-1)