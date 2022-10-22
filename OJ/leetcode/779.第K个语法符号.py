# 题目：779.第K个语法符号
# 难度：MEDIUM
# 最后提交：2022-10-20 00:24:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        l = 1<<(n-1)
        if k > l>>1:
            return self.kthGrammar(n-1, k-l//2) ^ 1
        else:
            return self.kthGrammar(n-1, k)