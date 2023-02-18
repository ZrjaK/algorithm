# 题目：2560.打家劫舍 IV
# 难度：MEDIUM
# 最后提交：2023-02-05 11:04:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(x):
            i = 0
            t = k
            while i < len(nums):
                if nums[i] <= x:
                    i += 2
                    t -= 1
                else:
                    i += 1
            return t <= 0
        l, r = 0, 1<<60
        while l + 1 < r:
            mid = l + r >> 1
            if check(mid):
                r = mid
            else:
                l = mid
        return r
        