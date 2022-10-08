# 题目：377.组合总和 Ⅳ
# 难度：MEDIUM
# 最后提交：2022-04-11 11:12:54 +0800 CST
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