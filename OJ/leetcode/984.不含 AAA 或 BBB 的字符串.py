# 题目：984.不含 AAA 或 BBB 的字符串
# 难度：MEDIUM
# 最后提交：2022-09-06 22:09:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        A, B = "a", "b"
        if a > b:
            a, b = b, a
            A, B = B, A
        if 2 * a > b:
            return (2*B+A) * (b-a) + (B+A) * (2*a-b)
        else:
            return (2*B+A) * a + B * (b-2*a)