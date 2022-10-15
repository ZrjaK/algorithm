# 题目：2132.用邮票贴满网格图
# 难度：HARD
# 最后提交：2022-10-11 15:42:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        h = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1] + grid[i][j]
        diff = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            x = i + stampHeight - 1
            for j in range(n):
                y = j + stampWidth - 1
                if x < m and y < n and h[x][y] - h[x][j-1] - h[i-1][y] + h[i-1][j-1] == 0:
                    diff[i][j] += 1
                    diff[i][y+1] -= 1
                    diff[x+1][j] -= 1
                    diff[x+1][y+1] += 1
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1] + diff[i][j]
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and not h[i][j]:
                    return False
        return True