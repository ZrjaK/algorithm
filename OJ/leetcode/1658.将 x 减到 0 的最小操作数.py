# 题目：1658.将 x 减到 0 的最小操作数
# 难度：MEDIUM
# 最后提交：2022-05-09 13:31:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        ans = -1
        l = 0
        t = 0
        for i in range(n):
            t += nums[i]
            while t > target and l < n:
                t -= nums[l]
                l += 1
            if t == target:
                ans = max(ans, i-l+1)
        return n-ans if ans >= 0 else -1