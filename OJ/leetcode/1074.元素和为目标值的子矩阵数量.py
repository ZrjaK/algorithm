# 题目：1074.元素和为目标值的子矩阵数量
# 难度：HARD
# 最后提交：2022-09-22 23:22:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        h = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1] + matrix[i][j]
        ans = 0
        for i1 in range(m):
            for i2 in range(i1, m):
                d = defaultdict(int)
                for j in range(n):
                    t = h[i2][j] - h[i1-1][j]
                    ans += d[t-target]
                    if t == target:
                        ans += 1
                    d[t] += 1
        return ans