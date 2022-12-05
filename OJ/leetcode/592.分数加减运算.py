# 题目：592.分数加减运算
# 难度：MEDIUM
# 最后提交：2022-11-23 10:05:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fractionAddition(self, expression: str) -> str:
        x, y = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            x1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x1 = x1 * 10 + int(expression[i])
                i += 1
            x1 = sign * x1
            i += 1

            # 读取分母
            y1 = 0
            while i < n and expression[i].isdigit():
                y1 = y1 * 10 + int(expression[i])
                i += 1

            x = x * y1 + x1 * y
            y *= y1
        if x == 0:
            return "0/1"
        g = gcd(abs(x), y)
        return f"{x // g}/{y // g}"