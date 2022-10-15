# 题目：剑指 Offer II 089.房屋偷盗
# 难度：MEDIUM
# 最后提交：2022-10-09 16:50:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def p(i):
            if i >= n:
                return 0
            return max(p(i+1), nums[i] + p(i+2))
        return p(0)