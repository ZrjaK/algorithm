# 题目：18.四数之和
# 难度：MEDIUM
# 最后提交：2022-05-26 00:25:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                l, r = j+1, n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return list(res)