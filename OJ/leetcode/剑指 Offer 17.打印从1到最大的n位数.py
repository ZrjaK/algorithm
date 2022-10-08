# 题目：剑指 Offer 17.打印从1到最大的n位数
# 难度：EASY
# 最后提交：2022-09-30 23:33:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10**n))