# 题目：537.复数乘法
# 难度：MEDIUM
# 最后提交：2022-11-21 22:06:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = num1.split("+")
        a1 = int(a1)
        b1 = int(b1[:-1])
        a2, b2 = num2.split("+")
        a2 = int(a2)
        b2 = int(b2[:-1])
        return f"{a1*a2-b1*b2}+{a1*b2+b1*a2}i"