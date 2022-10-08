# 题目：剑指 Offer II 002.二进制加法
# 难度：EASY
# 最后提交：2022-10-04 00:45:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]