# 题目：1498.满足条件的子序列数目
# 难度：MEDIUM
# 最后提交：2022-05-07 00:01:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l ,r, ans = 0, len(nums)-1, 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += 1<<r-l 
                ans %= int(1e9+7)
                l += 1
        return ans