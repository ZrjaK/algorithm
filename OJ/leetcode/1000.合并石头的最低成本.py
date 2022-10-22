# 题目：1000.合并石头的最低成本
# 难度：HARD
# 最后提交：2022-10-17 14:11:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        h = list(accumulate(stones)) + [0]
        @cache
        def p(l, r, c):
            if (r-l+1-c) % (k-1):
                return 1e99
            if l == r:
                return 0 if c == 1 else 1e99
            if c == 1:
                return p(l, r, k) + h[r] - h[l-1]
            res = 1e99
            for i in range(l, r):
                res = min(res, p(l, i, 1) + p(i+1, r, c-1))
            return res
        res = p(0, len(stones)-1, 1)
        p.cache_clear()
        return res if res < 1e90 else -1