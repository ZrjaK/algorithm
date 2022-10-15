# 题目：剑指 Offer II 101.分割等和子集
# 难度：EASY
# 最后提交：2022-10-10 10:10:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target*2 % 2 == 1:
            return False
        @cache
        def p(i, s):
            if s == target:
                return True
            if i > len(nums)-1:
                return False
            return p(i+1, s) or p(i+1, s + nums[i])
        return p(0, 0)