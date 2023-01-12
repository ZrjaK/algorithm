# 题目：1827.最少操作使数组递增
# 难度：EASY
# 最后提交：2022-12-11 02:15:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            ans += max(0, nums[i-1] + 1 - nums[i])
            nums[i] = max(nums[i], nums[i-1] + 1)
        return ans