# 题目：1765.地图中的最高点
# 难度：MEDIUM
# 最后提交：2022-08-12 00:52:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((0, i, j))
        res = [[1e99] * n for _ in range(m)]
        v = set()
        while q:
            s, x, y = q.popleft()
            if (x, y) in v:
                continue
            v.add((x, y))
            res[x][y] = min(res[x][y], s)
            for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0<=dx<m and 0<=dy<n:
                    q.append((res[x][y]+1, dx, dy))
        return res