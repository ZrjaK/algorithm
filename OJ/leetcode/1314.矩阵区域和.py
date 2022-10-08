# 题目：1314.矩阵区域和
# 难度：MEDIUM
# 最后提交：2022-09-12 20:38:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        h = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1] + mat[i][j]
        ans = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = h[min(i+k, m-1)][min(j+k, n-1)] - h[min(i+k, m-1)][max(0, j-k)-1] - h[max(0, i-k)-1][min(j+k, n-1)] + h[max(0, i-k)-1][max(0, j-k)-1]
        return ans