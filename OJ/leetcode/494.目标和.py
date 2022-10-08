# 题目：494.目标和
# 难度：MEDIUM
# 最后提交：2022-07-05 18:31:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def p(i, t):
            if i == len(nums):
                if t == target:
                    return 1
                else:
                    return 0
            res = p(i+1, t+nums[i]) + p(i+1, t-nums[i])
            return res
        return p(0, 0)