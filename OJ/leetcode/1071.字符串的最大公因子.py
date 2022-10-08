# 题目：1071.字符串的最大公因子
# 难度：EASY
# 最后提交：2021-11-06 14:31:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1 + str2 == str2 + str1 and str1[: math.gcd(len(str1), len(str2))] or ''