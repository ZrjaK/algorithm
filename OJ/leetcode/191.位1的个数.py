# 题目：191.位1的个数
# 难度：EASY
# 最后提交：2022-08-25 00:08:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()