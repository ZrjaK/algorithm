# 题目：2482.行和列中一和零的差值
# 难度：MEDIUM
# 最后提交：2022-11-27 01:45:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            onesRow = grid[i].count(1)
            zerosRow = grid[i].count(0)
            for j in range(m):
                ans[i][j] += onesRow - zerosRow
        for j in range(m):
            onesCol = [grid[i][j] for i in range(n)].count(1)
            zerosCol = [grid[i][j] for i in range(n)].count(0)
            for i in range(n):
                ans[i][j] += onesCol - zerosCol
        return ans