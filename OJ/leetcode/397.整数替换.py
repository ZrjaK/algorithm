# 题目：397.整数替换
# 难度：MEDIUM
# 最后提交：2022-07-02 18:12:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1 == 0:
            return 1 + self.integerReplacement(n>>1)
        if n & 3 == 3 and n != 3:
            return 1 + self.integerReplacement(n+1)
        return 1 + self.integerReplacement(n-1)