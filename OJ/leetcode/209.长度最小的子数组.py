# 题目：209.长度最小的子数组
# 难度：MEDIUM
# 最后提交：2022-04-20 14:19:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 1e99
        l = r = 0
        s = nums[0]
        while l < len(nums):
            print(l,r)
            if r+1 < len(nums) and (s < target or l > r):
                r += 1
                s += nums[r]
            else:
                if s >= target:
                    ans = min(ans, r-l+1)
                s -= nums[l]
                l += 1
        return int(ans % int(1e99))