# 题目：1556.千位分隔数
# 难度：EASY
# 最后提交：2021-10-20 00:57:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def thousandSeparator(self, n: int) -> str:
        list = []
        n = str(n)
        n = n[::-1]
        for i in range(0, len(n), 3):
            list.append(n[i:i+3])
        if len(n) > 3:
            n = ""
            for i in list:
                n += i + "."
            n = n[::-1]
            n = n[1:]
            return n
        else:
            return n[::-1]