# 题目：864.获取所有钥匙的最短路径
# 难度：HARD
# 最后提交：2022-11-10 09:55:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    q.append((0, i, j, 0))
                if grid[i][j] in "abcdef":
                    c += 1
        v = set()
        while q:
            s, x, y, key = q.popleft()
            if key.bit_count() == c:
                return s
            if (x, y, key) in v:
                continue
            v.add((x, y, key))
            for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] != "#":
                    if grid[nx][ny] in "abcdef":
                        q.append((s+1, nx, ny, key|1<<ord(grid[nx][ny])-97))
                    elif grid[nx][ny] in "ABCDEF":
                        if key>>ord(grid[nx][ny])-65 & 1:
                            q.append((s+1, nx, ny, key))
                    else:
                        q.append((s+1, nx, ny, key))
        return -1