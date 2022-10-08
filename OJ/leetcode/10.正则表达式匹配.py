# 题目：10.正则表达式匹配
# 难度：HARD
# 最后提交：2022-04-06 14:29:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) == 1 or p[1] != "*":
            return s != "" and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:])
        i = 0
        while i < len(s) and (s[i] == p[0] or p[0] == "."):
            if self.isMatch(s[i:], p[2:]):
                return True
            i += 1
        return self.isMatch(s[i:], p[2:])