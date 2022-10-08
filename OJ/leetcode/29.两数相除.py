# 题目：29.两数相除
# 难度：MEDIUM
# 最后提交：2022-08-24 16:42:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -1<<31 and divisor == -1:
            return (1<<31)-1
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res