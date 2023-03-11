# 题目：1590.使数组和能被 P 整除
# 难度：MEDIUM
# 最后提交：2023-03-10 09:37:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        d = {}
        f = sum(nums) % p
        ans = n
        c = 0
        for i in range(n):
            c += nums[i]
            t = c % p
            d[t] = i
            if t == f:
                ans = min(ans, i+1)
            if (t-f+p)%p in d:
                ans = min(ans, i-d[(t-f+p)%p])
        return ans if ans != n else -1