# 题目：840.矩阵中的幻方
# 难度：MEDIUM
# 最后提交：2022-09-12 14:08:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                ans += sorted([grid[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2)]) == [1,2,3,4,5,6,7,8,9] and all(map(lambda x: x==15, [
                    grid[i-1][j-1]+grid[i][j]+grid[i+1][j+1], 
                    grid[i-1][j+1]+grid[i][j]+grid[i+1][j-1],

                    grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1],
                    grid[i][j-1]+grid[i][j]+grid[i][j+1],
                    grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1],

                    grid[i-1][j-1]+grid[i][j-1]+grid[i+1][j-1],
                    grid[i-1][j]+grid[i][j]+grid[i+1][j],
                    grid[i-1][j+1]+grid[i][j+1]+grid[i+1][j+1],]))
            
        return ans