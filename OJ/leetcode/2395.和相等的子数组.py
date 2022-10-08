# 题目：2395.和相等的子数组
# 难度：EASY
# 最后提交：2022-09-03 22:31:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        v = set()
        for i in range(n-1):
            if nums[i] + nums[i+1] in v:
                return True
            v.add(nums[i] + nums[i+1])
        return False