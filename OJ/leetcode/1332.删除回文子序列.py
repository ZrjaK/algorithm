# 题目：1332.删除回文子序列
# 难度：EASY
# 最后提交：2022-06-08 04:32:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2