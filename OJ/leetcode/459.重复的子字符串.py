# 题目：459.重复的子字符串
# 难度：EASY
# 最后提交：2021-10-22 12:23:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

