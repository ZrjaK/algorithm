# 题目：190.颠倒二进制位
# 难度：EASY
# 最后提交：2022-08-25 00:02:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reverseBits(self, n: int) -> int:
        t = bin(n)[2:]
        if len(t) < 32:
            t = "0" * (32-len(t)) + t
        return int(t[::-1], 2)