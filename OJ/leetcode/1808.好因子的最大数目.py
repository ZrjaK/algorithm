# 题目：1808.好因子的最大数目
# 难度：HARD
# 最后提交：2022-09-17 11:58:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        a, b = primeFactors // 3, primeFactors % 3
        if b == 1:
            res = pow(3, a-1, int(1e9+7)) * 4 
        elif b == 2:
            res = pow(3, a, int(1e9+7)) * 2
        else:
            res = pow(3, a, int(1e9+7))
        return res % int(1e9+7)