# 题目：516.最长回文子序列
# 难度：MEDIUM
# 最后提交：2022-09-22 16:19:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def p(i, j):
            if i >= j:
                return i == j
            if s[i] == s[j]:
                return 2 + p(i+1, j-1)
            return max(p(i+1, j), p(i, j-1))
        return int(p(0, len(s)-1))