# 题目：2104.子数组范围和
# 难度：MEDIUM
# 最后提交：2022-09-05 10:11:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ma = mi = nums[i]
            for j in range(i+1, n):
                ma = max(ma, nums[j])
                mi = min(mi, nums[j])
                ans += ma - mi
        return ans