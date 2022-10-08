# 题目：279.完全平方数
# 难度：MEDIUM
# 最后提交：2022-06-23 00:20:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def p(i):
            if i == 0:
                return 0
            m = 1e99
            for j in range(1, int(i**0.5)+1):
                m = min(m, p(i-j*j))
            return m + 1
        return p(n)