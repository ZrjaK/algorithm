# 题目：2485.找出中枢整数
# 难度：EASY
# 最后提交：2022-11-27 12:22:10 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            if (1 + i) * i // 2 == (i + n) * (n-i+1) // 2:
                return i
        return -1