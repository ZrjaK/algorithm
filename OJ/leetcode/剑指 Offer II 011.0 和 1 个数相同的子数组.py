# 题目：剑指 Offer II 011.0 和 1 个数相同的子数组
# 难度：MEDIUM
# 最后提交：2022-10-04 16:24:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        h = list(accumulate(nums))
        d = {0: -1}
        ans = 0
        for i in range(n):
            if h[i] in d:
                ans = max(ans, i-d[h[i]])
            else:
                d[h[i]] = i
        return ans