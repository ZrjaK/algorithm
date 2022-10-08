# 题目：50.Pow(x, n)
# 难度：MEDIUM
# 最后提交：2022-09-17 11:47:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        res = 1
        if n % 2:
            res *= x
            n -= 1
        f = self.myPow(x, n>>1)
        return res * f * f