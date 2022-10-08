# 题目：62.不同路径
# 难度：MEDIUM
# 最后提交：2022-08-08 08:19:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]