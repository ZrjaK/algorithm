# 题目：688.骑士在棋盘上的概率
# 难度：MEDIUM
# 最后提交：2022-07-06 23:38:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def p(i, j, rest):
            if not (0 <= i < n and 0 <= j < n):
                return [0, 8**rest]
            if rest == 0:
                return [1, 1]
            res = [0, 0]
            p1 = p(i-2, j+1, rest-1)
            p2 = p(i-2, j-1, rest-1)
            p3 = p(i+2, j+1, rest-1)
            p4 = p(i+2, j-1, rest-1)
            p5 = p(i-1, j+2, rest-1)
            p6 = p(i-1, j-2, rest-1)
            p7 = p(i+1, j+2, rest-1)
            p8 = p(i+1, j-2, rest-1)
            res[0] = p1[0]+p2[0]+p3[0]+p4[0]+p5[0]+p6[0]+p7[0]+p8[0]
            res[1] = p1[1]+p2[1]+p3[1]+p4[1]+p5[1]+p6[1]+p7[1]+p8[1]
            return res
        res = p(row, column, k)
        return res[0] / res[1]