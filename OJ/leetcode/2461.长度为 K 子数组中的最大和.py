# 题目：2461.长度为 K 子数组中的最大和
# 难度：MEDIUM
# 最后提交：2022-11-06 10:37:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = s = 0
        v = set()
        for r in range(n):
            while nums[r] in v:
                v.remove(nums[l])
                s -= nums[l]
                l += 1
            s += nums[r]
            v.add(nums[r])
            while len(v) > k:
                v.remove(nums[l])
                s -= nums[l]
                l += 1
            if len(v) == k:
                ans = max(ans, s)
        return ans
        