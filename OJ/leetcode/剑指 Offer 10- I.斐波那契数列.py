# 题目：剑指 Offer 10- I.斐波那契数列
# 难度：EASY
# 最后提交：2022-09-30 11:11:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return (self.fib(n-1) + self.fib(n-2)) % int(1e9+7)