# 题目：剑指 Offer 14- I.剪绳子
# 难度：MEDIUM
# 最后提交：2022-09-30 23:26:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        a, b = n // 3, n % 3
        if b == 0:
            return 3 ** a
        if b == 1:
            return 3 ** (a-1) * 4
        else:
            return 3 ** a * 2