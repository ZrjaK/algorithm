# 题目：1304.和为零的 N 个不同整数
# 难度：EASY
# 最后提交：2022-04-03 16:17:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumZero(self, n: int) -> List[int]:
        r = []
        for i in range(1, n//2+1):
            r.append(i)
            r.append(-i)
        if n % 2 == 1:
            r.append(0)
        return r