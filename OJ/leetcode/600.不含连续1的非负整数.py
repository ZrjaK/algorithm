# 题目：600.不含连续1的非负整数
# 难度：HARD
# 最后提交：2022-09-15 10:27:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]
        @cache
        def p(i, islimit, preis1):
            if i == len(s):
                return 1
            up = int(s[i]) if islimit else 1
            res = p(i+1, islimit and up == 0, False)
            if not preis1 and up == 1:
                res += p(i+1, islimit, True)
            return res
        return p(0, True, False)