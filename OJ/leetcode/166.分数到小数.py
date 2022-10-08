# 题目：166.分数到小数
# 难度：MEDIUM
# 最后提交：2022-10-03 16:53:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        # 整数部分
        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        # 小数部分
        indexMap = {}
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:  # 有循环节
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)