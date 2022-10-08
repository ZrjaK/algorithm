# 题目：918.环形子数组的最大和
# 难度：MEDIUM
# 最后提交：2022-03-25 04:35:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pre, ma, mi = nums[0], nums[0], 0
        for i in range(1,len(nums)):
            pre = max(nums[i], pre+nums[i])
            ma = max(ma, pre)
        pre = 0
        for i in range(1, len(nums)-1):
            pre = min(nums[i], pre+nums[i])
            mi = min(mi, pre)
        return max(ma, sum(nums)-mi)