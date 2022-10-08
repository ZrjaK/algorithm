# 题目：461.汉明距离
# 难度：EASY
# 最后提交：2021-10-22 12:34:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')