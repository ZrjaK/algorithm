# 题目：1269.停在原地的方案数
# 难度：HARD
# 最后提交：2022-10-24 12:06:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def p(i, rest):
            if rest == 0:
                return int(i == 0)
            res = p(i, rest-1)
            if i:
                res += p(i-1, rest-1)
            if i+1 < arrLen:
                res += p(i+1, rest-1)
            return res
        return p(0, steps) % int(1e9+7)