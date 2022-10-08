# 题目：214.最短回文串
# 难度：HARD
# 最后提交：2022-04-05 23:37:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        t = s[::-1]
        for i in range(len(s)):
            k = t[:i] + s
            if k == k[::-1]:
                return k
            