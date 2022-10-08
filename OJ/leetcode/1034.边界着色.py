# 题目：1034.边界着色
# 难度：MEDIUM
# 最后提交：2022-08-05 03:11:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        originalColor = grid[row][col]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque([(row, col)])
        visited[row][col] = True
        while q:
            x, y = q.popleft()
            isBorder = False
            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                    isBorder = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            if isBorder:
                borders.append((x, y))
        for x, y in borders:
            grid[x][y] = color
        return grid