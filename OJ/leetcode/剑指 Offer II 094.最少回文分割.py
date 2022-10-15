# 题目：剑指 Offer II 094.最少回文分割
# 难度：HARD
# 最后提交：2022-10-09 19:36:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        @cache
        def check(i, j):
            if i >= j:
                return True
            if s[i] == s[j]:
                return check(i+1, j-1)
            return False
        @cache
        def p(i):
            if i == n:
                return 0
            res = 1e99
            for j in range(i, n):
                if check(i, j):
                    res = min(res, 1 + p(j+1))
            return res
        return p(0) - 1