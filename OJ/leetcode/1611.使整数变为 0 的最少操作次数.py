# 题目：1611.使整数变为 0 的最少操作次数
# 难度：HARD
# 最后提交：2022-09-29 10:41:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        for i in range(31, -1, -1):
            if n>>i & 1:
                return (1<<i+1)-1 - self.minimumOneBitOperations(n-(1<<i))