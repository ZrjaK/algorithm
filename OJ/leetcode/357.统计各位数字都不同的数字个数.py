# 题目：357.统计各位数字都不同的数字个数
# 难度：MEDIUM
# 最后提交：2022-04-11 00:24:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @lru_cache(None)
        def nt(n):
            s = 1
            for i in range(1,n+1):
                s *= i
            return s
        def p(n):
            if n == 0:
                return 1
            return 9*nt(9)//nt(9-n+1) + p(n-1)
        return p(n)