# 题目：902.最大为 N 的数字组合
# 难度：HARD
# 最后提交：2022-09-15 10:29:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        @cache
        def p(i, islimit, isnum):
            if i == len(s):
                return int(isnum)
            res = 0
            if not isnum:
                res = p(i+1, False, False)
            up = s[i] if islimit else digits[-1]
            for j in digits:
                if j <= up:
                    res += p(i+1, islimit and j == up, True)
            return res
        return p(0, True, False)