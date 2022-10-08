# 题目：2193.得到回文串的最少操作次数
# 难度：HARD
# 最后提交：2022-09-19 10:46:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        if len(s) <= 2:
            return 0
        n = len(s)
        for i in range(n-1, 0, -1):
            if s[i] == s[0]:
                break
        else:
            return n // 2 + self.minMovesToMakePalindrome(s[1:])
        return n - 1 - i + self.minMovesToMakePalindrome(s[1:i]+s[i+1:])