# 题目：1800.最大升序子数组和
# 难度：EASY
# 最后提交：2022-10-07 00:09:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums += [0]
        n = len(nums)
        s = 0
        ans = 0
        for i in range(n):
            if nums[i] > nums[i-1]:
                s += nums[i]
            else:
                s = nums[i]
            ans = max(ans, s)
        return ans