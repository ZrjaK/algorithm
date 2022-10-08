# 题目：1689.十-二进制数的最少数目
# 难度：MEDIUM
# 最后提交：2022-09-07 11:49:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))