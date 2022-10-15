# 题目：剑指 Offer II 102.加减的目标值
# 难度：MEDIUM
# 最后提交：2022-10-10 10:26:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def p(i, c):
            if i == n:
                return int(c == target)
            return p(i+1, c + nums[i]) + p(i+1, c - nums[i])
        return p(0, 0)