# 题目：1799.N 次操作后的最大分数和
# 难度：HARD
# 最后提交：2022-09-17 12:16:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def p(arr, k):
            if k > n//2:
                return 0
            res = -1e99
            for i in range(n):
                for j in range(i+1, n):
                    if arr>>i & 1 == arr>>j & 1 == 0:
                        res = max(res, k * gcd(nums[i], nums[j]) + p(arr|1<<i|1<<j,k+1))
            return res
        return p(1<<n, 1)