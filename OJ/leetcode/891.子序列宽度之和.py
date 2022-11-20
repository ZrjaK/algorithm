# 题目：891.子序列宽度之和
# 难度：HARD
# 最后提交：2022-11-18 09:31:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            ans += nums[i] * pow(2, i, int(1e9+7))
            ans -= nums[i] * pow(2, n-i-1, int(1e9+7))
        return ans % int(1e9+7)