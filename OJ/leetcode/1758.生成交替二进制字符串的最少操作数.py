# 题目：1758.生成交替二进制字符串的最少操作数
# 难度：EASY
# 最后提交：2022-11-29 15:45:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t1 = "01" * n
        t2 = "10" * n
        return min(len([i for i in range(n) if s[i] != t1[i]]), len([i for i in range(n) if s[i] != t2[i]]))