# 题目：1263.推箱子
# 难度：HARD
# 最后提交：2022-09-27 23:18:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def check(cx, cy, i, j, x, y):
            if not (0<=cx<m and 0<=cy<n) or grid[cx][cy] == "#":
                return False
            q = deque([[x, y]])
            v = set()
            while q:
                x, y = q.popleft()
                if (x, y) == (cx, cy):
                    return True
                if (x, y) in v:
                    continue
                v.add((x, y))
                for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != "#" and (x, y) != (i, j):
                        q.append([nx, ny])
            return False
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "B":
                    for x in range(m):
                        for y in range(n):
                            if grid[x][y] == "S":
                                q = deque([[0, i, j, x, y]])
                                break
        v = set()
        while q:
            s, i, j, x, y = q.popleft()
            if grid[i][j] == "T":
                return s
            if (i, j, x, y) in v:
                continue
            v.add((i, j, x, y))
            for nx, ny, cx, cy in [[i-1, j, i+1, j], [i+1, j, i-1, j], \
                                    [i, j+1, i, j-1], [i, j-1, i, j+1]]:
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] != "#" and check(cx, cy, i, j, x, y):
                    q.append([s+1, nx, ny, i, j])
        return -1