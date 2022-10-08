# 题目：1770.执行乘法运算的最大分数
# 难度：HARD
# 最后提交：2022-09-17 11:06:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

import gc;gc.disable()
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        @cache
        def p(i, j, idx):
            if idx == m:
                return 0
            r1 = multipliers[idx] * nums[i] + p(i+1, j, idx+1)
            r2 = multipliers[idx] * nums[j] + p(i, j-1, idx + 1)
            return max(r1, r2)
        res = p(0, n-1, 0)
        p.cache_clear()
        return res