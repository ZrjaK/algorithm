# 题目：1312.让字符串成为回文串的最少插入次数
# 难度：HARD
# 最后提交：2022-10-24 12:12:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def p(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return p(i+1, j-1)
            return 1 + min(p(i+1, j), p(i, j-1))
        return p(0, len(s)-1)