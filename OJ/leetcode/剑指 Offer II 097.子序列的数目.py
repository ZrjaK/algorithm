# 题目：剑指 Offer II 097.子序列的数目
# 难度：HARD
# 最后提交：2022-10-10 09:16:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def p(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            res = p(i+1, j)
            if s[i] == t[j]:
                res += p(i+1, j+1)
            return res
        return p(0, 0)