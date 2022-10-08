# 题目：1009.十进制整数的反码
# 难度：EASY
# 最后提交：2021-11-03 19:34:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (1 << (len(bin(n)) - 2))- 1 - n