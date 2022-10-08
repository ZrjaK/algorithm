# 题目：972.相等的有理数
# 难度：HARD
# 最后提交：2022-09-19 22:42:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:  
        if "(" in s:
            l = s.index("(")
            r = s.index(")")
            s = s[:l] + s[l+1:r] * 20
        if "(" in t:
            l = t.index("(")
            r = t.index(")")
            t = t[:l] + t[l+1:r] * 20
        return float(s) == float(t)
        