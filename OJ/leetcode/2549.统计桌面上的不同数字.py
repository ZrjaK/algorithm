# 题目：2549.统计桌面上的不同数字
# 难度：EASY
# 最后提交：2023-01-29 16:46:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1