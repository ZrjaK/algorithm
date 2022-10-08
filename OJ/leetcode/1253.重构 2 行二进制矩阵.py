# 题目：1253.重构 2 行二进制矩阵
# 难度：MEDIUM
# 最后提交：2022-09-06 08:59:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        res = [[0] * n for _ in range(2)]
        for i in range(n):
            if not colsum[i]:
                continue
            if colsum[i] > 2:
                return []
            if colsum[i] == 2:
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1
                lower -= 1
            if colsum[i] == 1:
                if upper > lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        if lower or upper:
            return []
        return res