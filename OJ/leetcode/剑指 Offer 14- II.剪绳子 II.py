# 题目：剑指 Offer 14- II.剪绳子 II
# 难度：MEDIUM
# 最后提交：2022-09-30 23:28:17 +0800 CST
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
            return pow(3, a, 10**9+7)
        if b == 1:
            return pow(3, a-1, 10**9+7) * 4 % (10**9+7)
        else:
            return pow(3, a, 10**9+7) * 2 % (10**9+7)