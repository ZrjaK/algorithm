# 题目：201.数字范围按位与
# 难度：MEDIUM
# 最后提交：2022-08-25 00:24:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 32
        while i >= 0:
            if left & 1<<i and right & 1<<i:
                break
            if (left & 1<<i) ^ (right & 1<<i):
                return 0
            i -= 1
        res = 0
        while i >= 0:
            if (left & 1<<i) ^(right & 1<<i):
                break
            res |= 1<<i & left
            i -= 1
        return res