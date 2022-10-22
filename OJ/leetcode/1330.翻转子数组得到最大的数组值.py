# 题目：1330.翻转子数组得到最大的数组值
# 难度：HARD
# 最后提交：2022-10-19 14:13:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        base = sum([abs(nums[i]-nums[i+1]) for i in range(n-1)])
        ans = base
        for i in range(n-1):
            ans = max(ans, base - abs(nums[i]-nums[i+1]) + abs(nums[i]-nums[-1]))
        for i in range(n-1):
            ans = max(ans, base - abs(nums[i]-nums[i+1]) + abs(nums[i+1]-nums[0]))
        mi_ma = max(min(nums[i], nums[i+1]) for i in range(n-1))
        ma_mi = min(max(nums[i], nums[i+1]) for i in range(n-1))
        ans = max(ans, base + 2 * (mi_ma - ma_mi))
        return ans