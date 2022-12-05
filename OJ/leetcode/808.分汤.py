# 题目：808.分汤
# 难度：MEDIUM
# 最后提交：2022-11-21 13:21:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        @cache
        def p(resta, restb):
            if resta <= 0:
                if restb <= 0:
                    return 0.5
                else:
                    return 1
            if restb <= 0:
                return 0
            return 0.25 * (p(resta-100, restb) + p(resta-75, restb-25) +
                             p(resta-50, restb-50) + p(resta-25, restb-75))
        return p(n, n)