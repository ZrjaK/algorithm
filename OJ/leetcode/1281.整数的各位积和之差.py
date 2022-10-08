# 题目：1281.整数的各位积和之差
# 难度：EASY
# 最后提交：2022-05-01 14:27:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        t = [int(i) for i in str(n)]
        s = 1
        for i in t:
            s *= i
        return s - sum(t)