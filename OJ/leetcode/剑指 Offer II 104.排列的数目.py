# 题目：剑指 Offer II 104.排列的数目
# 难度：MEDIUM
# 最后提交：2022-10-10 11:36:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @lru_cache(None)
        def p(tar):
            if tar < 0:
                return 0
            if tar == 0:
                return 1
            res = 0
            for i in nums:
                res += p(tar-i)
            return res
        return p(target)