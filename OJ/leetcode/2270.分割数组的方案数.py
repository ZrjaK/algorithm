# 题目：2270.分割数组的方案数
# 难度：MEDIUM
# 最后提交：2022-05-14 22:35:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        h = list(accumulate(nums))
        n = len(nums)
        ans = 0
        for i in range(n-1):
            if h[i] >= h[-1]-h[i]:
                ans += 1
        return ans