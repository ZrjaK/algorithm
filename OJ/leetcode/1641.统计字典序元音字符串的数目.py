# 题目：1641.统计字典序元音字符串的数目
# 难度：MEDIUM
# 最后提交：2022-07-19 03:29:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def p(x, i):
            if i == 1:
                return x
            if x == 0:
                return 0
            res = 0
            for j in range(1, x+1):
                res += p(j, i-1)
            return res
        return p(5, n)