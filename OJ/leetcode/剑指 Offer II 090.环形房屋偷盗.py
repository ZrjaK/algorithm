# 题目：剑指 Offer II 090.环形房屋偷盗
# 难度：MEDIUM
# 最后提交：2022-10-09 16:55:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def p(i, steal0):
            if i >= n:
                return 0
            if i == n-1:
                if steal0:
                    return 0
                return nums[n-1]
            return max(p(i+1, steal0), nums[i] + p(i+2, steal0|(i == 0)))
        return p(0, False)