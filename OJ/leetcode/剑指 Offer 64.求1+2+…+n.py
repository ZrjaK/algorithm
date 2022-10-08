# 题目：剑指 Offer 64.求1+2+…+n
# 难度：MEDIUM
# 最后提交：2022-10-03 21:07:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n-1)