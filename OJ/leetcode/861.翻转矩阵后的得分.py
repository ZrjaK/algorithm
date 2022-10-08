# 题目：861.翻转矩阵后的得分
# 难度：MEDIUM
# 最后提交：2022-04-24 08:17:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] ^= 1
        for j in range(1, m):
            n0 = n1 = 0
            for i in range(n):
                if grid[i][j] == 1:
                    n1 += 1
                else:
                    n0 += 1
            if n0 > n1:
                for i in range(n):
                    grid[i][j] ^= 1
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += grid[i][j]* 2 **(m-1-j)
        return ans