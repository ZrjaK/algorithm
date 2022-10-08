# 题目：363.矩形区域不超过 K 的最大数值和
# 难度：HARD
# 最后提交：2022-09-22 23:33:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        h = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1] + matrix[i][j]
        ans = -1e99
        for i1 in range(m):
            for i2 in range(i1, m):
                d = [0]
                for j in range(n):
                    t = h[i2][j] - h[i1-1][j]
                    f = bisect_left(d, t-k)
                    if f < len(d):
                        ans = max(ans, t-d[f])
                    insort(d, t)
        return ans