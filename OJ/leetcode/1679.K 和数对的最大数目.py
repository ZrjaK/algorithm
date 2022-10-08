# 题目：1679.K 和数对的最大数目
# 难度：MEDIUM
# 最后提交：2022-04-10 06:39:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        ans = 0
        while l < r:
            t = nums[l] + nums[r]
            if t < k:
                l += 1
            elif t > k:
                r -= 1
            else:
                ans += 1
                l += 1
                r -= 1
        return ans