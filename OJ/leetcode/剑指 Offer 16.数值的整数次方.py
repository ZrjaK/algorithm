# 题目：剑指 Offer 16.数值的整数次方
# 难度：MEDIUM
# 最后提交：2022-09-30 23:32:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(i):
            if not i:
                return 1
            t = p(i//2)
            return t * t if i % 2 == 0 else t * t * x
        return p(n) if n > 0 else 1 / p(-n)