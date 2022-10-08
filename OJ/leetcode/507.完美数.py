# 题目：507.完美数
# 难度：EASY
# 最后提交：2021-10-22 15:07:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 0
        for i in range(2, int(sqrt(num))+1):
            if i * (num // i) == num:
                s += i + num // i
        return s+1 == num