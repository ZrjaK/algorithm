# 题目：2258.逃离火灾
# 难度：HARD
# 最后提交：2022-09-29 12:29:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        v = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((0, i, j))
        h = [[1e99] * n for _ in range(m)]
        while q:
            s, x, y = q.popleft()
            if (x, y) in v:
                continue
            v.add((x, y))
            h[x][y] = s
            for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 0:
                    q.append((s+1, nx, ny))
        def check(t):
            q = deque([[t, 0, 0]])
            v = set()
            while q:
                s, x, y = q.popleft()
                if (x, y) == (m-1, n-1) and s <= h[x][y]:
                    return True
                if s >= h[x][y]:
                    continue
                if (x, y) in v:
                    continue
                v.add((x, y))
                for nx, ny in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 0:
                        q.append((s+1, nx, ny))
            return False
        l, r = -1, 10**9
        while l <= r:
            mid = l+r>>1
            if not check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return max(-1, r)