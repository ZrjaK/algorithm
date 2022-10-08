# 题目：258.各位相加
# 难度：EASY
# 最后提交：2021-10-21 15:31:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def addDigits(self, num: int) -> int:
        s = num
        while s >= 10:
            s = 0
            for i in str(num):
                s += int(i)
            num = s
        return s