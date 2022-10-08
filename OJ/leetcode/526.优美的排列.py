# 题目：526.优美的排列
# 难度：MEDIUM
# 最后提交：2022-07-05 19:04:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def p(i, rest):
            if rest == 0:
                return 1
            res = 0
            for j in range(16):
                if 1<<j & rest and (i % j == 0 or j % i == 0):
                    res += p(i+1, rest^1<<j)
            return res
        return p(1, (1<<n+1)-2)