# 题目：2429.最小 XOR
# 难度：MEDIUM
# 最后提交：2022-10-02 10:36:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c = num1
        num2 = num2.bit_count()
        for i in range(31, -1, -1):
            if num2 and c>>i & 1:
                c ^= 1<<i
                num2 -= 1
        for i in range(32):
            if num2 and not num1>>i & 1:
                c |= 1<<i
                num2 -= 1
        return c ^ num1