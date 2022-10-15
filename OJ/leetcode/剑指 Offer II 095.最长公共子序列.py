# 题目：剑指 Offer II 095.最长公共子序列
# 难度：MEDIUM
# 最后提交：2022-10-09 19:47:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def p(i, j):
            if i == n or j == m:
                return 0
            res = 0
            if text1[i] == text2[j]:
                res = max(res, 1 + p(i+1, j+1))
            res = max(res, p(i+1, j), p(i, j+1))
            return res
        return p(0, 0)