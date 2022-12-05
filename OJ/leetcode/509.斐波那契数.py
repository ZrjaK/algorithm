# 题目：509.斐波那契数
# 难度：EASY
# 最后提交：2022-11-21 15:48:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fib(self, n: int) -> int:
        def powMatrix(m, p):
            res = [[0] * len(m[0]) for _ in range(len(m))]
            for i in range(len(m)):
                res[i][i] = 1
            t = m
            while p:
                if p & 1:
                    res = mulMatrix(res, t)
                t = mulMatrix(t, t)
                p >>= 1
            return res

        def mulMatrix(m1, m2):
            res = [[0] * len(m2[0]) for _ in range(len(m1))]
            for i in range(len(m1)):
                for j in range(len(m2[0])):
                    for k in range(len(m2)):
                        res[i][j] += m1[i][k] * m2[k][j]
            return res

        if n <= 1:
            return n
        m = [[1, 1], [1, 0]]
        res = powMatrix(m, n-2)
        return res[0][0] + res[1][0]