# 题目：1162.地图分析
# 难度：MEDIUM
# 最后提交：2022-07-13 14:26:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if all(all(j == 1 for j in i) for i in grid) or all(all(j == 0 for j in i) for i in grid):
            return -1
        m, n = len(grid), len(grid[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q.append([i, j])
        while q:
            x, y = q.popleft()
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < m and 0 <= yy < n and not grid[xx][yy]:
                    grid[xx][yy] = grid[x][y] + 1
                    q.append([xx, yy])
        return grid[x][y]-1