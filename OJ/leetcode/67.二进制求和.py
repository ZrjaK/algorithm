# 题目：67.二进制求和
# 难度：EASY
# 最后提交：2021-10-20 19:54:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]