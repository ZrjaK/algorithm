# 题目：343.整数拆分
# 难度：MEDIUM
# 最后提交：2022-06-29 19:37:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def p(i):
            if i == 2:
                return 1
            res = -1e99
            for j in range(1, i//2+1):
                res = max(res, j*p(i-j), j*(i-j))
            return res
            
        return p(n)