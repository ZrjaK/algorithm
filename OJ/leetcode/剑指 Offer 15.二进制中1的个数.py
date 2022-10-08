# 题目：剑指 Offer 15.二进制中1的个数
# 难度：EASY
# 最后提交：2022-09-30 23:28:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()