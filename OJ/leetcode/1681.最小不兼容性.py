# 题目：1681.最小不兼容性
# 难度：HARD
# 最后提交：2022-10-13 19:36:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        if max(Counter(nums).values()) > k:
            return -1
        c = len(nums) // k
        n = len(nums)
        @cache
        def p(mask):
            if mask + 1 == 1<<n:
                return 0
            res = 1e99
            d = {nums[i]: i for i in range(n) if not mask>>i & 1}
            for lst in combinations(d.keys(), c):
                t = sum(1<<d[i] for i in lst)
                res = min(res, max(lst)-min(lst)+p(mask|t))
            return res
        return p(0)