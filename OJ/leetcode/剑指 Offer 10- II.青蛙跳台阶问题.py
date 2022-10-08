# 题目：剑指 Offer 10- II.青蛙跳台阶问题
# 难度：EASY
# 最后提交：2022-09-30 11:12:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    @cache
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        return (self.numWays(n-1) + self.numWays(n-2)) % int(1e9+7)