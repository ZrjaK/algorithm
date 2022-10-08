# 题目：2091.从数组中移除最大值和最小值
# 难度：MEDIUM
# 最后提交：2022-09-09 17:20:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        ma = max(nums)
        a = [i for i in range(n) if nums[i] == ma]
        mi = min(nums)
        b = [i for i in range(n) if nums[i] == mi]
        return min(1+max(a[0], b[0]), n-min(a[-1], b[-1]), 1+a[0]+n-b[-1], 1+b[0]+n-a[-1])