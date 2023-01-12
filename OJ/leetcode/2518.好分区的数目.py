# 题目：2518.好分区的数目
# 难度：HARD
# 最后提交：2022-12-25 19:29:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0
        n = len(nums)
        @cache
        def p(i, s):
            if s < 0:
                return 0
            if i == n:
                return int(s == 0)
            return (p(i+1, s) + p(i+1, s-nums[i])) % int(1e9+7)
        res = (pow(2, n, int(1e9+7)) - 2*sum(p(0, i) for i in range(k))) % int(1e9+7)
        p.cache_clear()
        return res
        