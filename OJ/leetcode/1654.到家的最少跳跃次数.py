# 题目：1654.到家的最少跳跃次数
# 难度：MEDIUM
# 最后提交：2022-07-19 18:37:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        fs = set(forbidden)
        v = set()
        @cache
        def p(i, canback):
            if i in fs or i > 6000 or i < 0 or i in v:
                return 1e99
            if i == x:
                return 0
            v.add(i)
            res = p(i+a, True)
            if canback:
                res = min(res, p(i-b, False))
            v.remove(i)
            return res + 1
        res = p(0, False)
        return res if res < 1e90 else -1