# 题目：87.扰乱字符串
# 难度：HARD
# 最后提交：2022-10-03 14:57:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def p(s, t):
            if Counter(s) != Counter(t):
                return False
            if len(s) == 1:
                return True
            n = len(s)
            for i in range(1, n):
                if p(s[:i], t[:i]) and p(s[i:], t[i:]):
                    return True
                if p(s[:i], t[-i:]) and p(s[i:], t[:-i]):
                    return True
            return False
        return p(s1, s2)