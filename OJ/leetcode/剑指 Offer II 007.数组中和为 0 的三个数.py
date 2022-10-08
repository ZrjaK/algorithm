# 题目：剑指 Offer II 007.数组中和为 0 的三个数
# 难度：MEDIUM
# 最后提交：2022-10-04 10:46:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i and nums[i] == nums[i-1]:
                continue
            k = n-1
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
        return ans