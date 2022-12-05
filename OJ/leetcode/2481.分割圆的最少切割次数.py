# 题目：2481.分割圆的最少切割次数
# 难度：EASY
# 最后提交：2022-11-27 01:40:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2 == 0 or n == 1:
            return n // 2
        return n