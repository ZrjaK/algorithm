# 题目：409.最长回文串
# 难度：EASY
# 最后提交：2021-10-21 20:11:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s1 = 0
        for i in set(s):
            s1 += s.count(i) % 2
        return len(s) - max(0, s1 - 1)