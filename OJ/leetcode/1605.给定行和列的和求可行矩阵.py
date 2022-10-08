# 题目：1605.给定行和列的和求可行矩阵
# 难度：MEDIUM
# 最后提交：2022-09-07 10:53:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res