# 题目：1881.插入后的最大值
# 难度：MEDIUM
# 最后提交：2022-09-08 10:51:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        l = len(n)
        if n[0] == '-':
            for i in range(1, l):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i in range(l):
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)