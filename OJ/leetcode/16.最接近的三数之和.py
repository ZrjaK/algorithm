# 题目：16.最接近的三数之和
# 难度：MEDIUM
# 最后提交：2022-05-26 00:17:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 1e99
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s-target) < abs(ans-target):
                    ans = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
        return ans
