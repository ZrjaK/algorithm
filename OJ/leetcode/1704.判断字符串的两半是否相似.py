# 题目：1704.判断字符串的两半是否相似
# 难度：EASY
# 最后提交：2022-11-11 16:01:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        c1 = 0
        c2 = 0
        for i in s[:n//2]:
            if i in "aeiouAEIOU":
                c1 += 1
        for i in s[n//2:]:
            if i in "aeiouAEIOU":
                c2 += 1
        return c1 == c2