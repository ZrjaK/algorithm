# 题目：680.验证回文串 II
# 难度：EASY
# 最后提交：2021-10-23 12:57:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                a = s[l + 1 : r + 1]
                b = s[l:r]
                return a == a[::-1] or b==b[::-1]