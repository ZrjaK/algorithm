# 题目：2220.转换数字的最少位翻转次数
# 难度：EASY
# 最后提交：2022-04-02 22:32:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start^goal)[2:]
        return a.count("1")