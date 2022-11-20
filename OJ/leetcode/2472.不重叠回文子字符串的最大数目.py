# 题目：2472.不重叠回文子字符串的最大数目
# 难度：HARD
# 最后提交：2022-11-14 11:09:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

import gc;gc.disable()
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def check(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return check(i+1, j-1)
        @cache
        def p(i):
            if i == n:
                return 0
            res = p(i+1)
            for j in range(i+k-1, n):
                if check(i, j):
                    res = max(res, 1 + p(j+1))
            return res
        res = p(0)
        p.cache_clear()
        check.cache_clear()
        return res