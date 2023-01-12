# 题目：2503.矩阵查询可获得的最大分数
# 难度：HARD
# 最后提交：2022-12-11 14:05:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        queries = [[i, v] for i, v in enumerate(queries)]
        queries.sort(key=lambda x: -x[1])
        ans = [0] * len(queries)
        pq = [(grid[0][0], 0, 0)]
        v = set([(0, 0)])
        anss = 0
        while queries:
            t = queries.pop()
            while pq and pq[0][0] < t[1]:
                _, x, y = heappop(pq)
                anss += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m and (nx, ny) not in v:
                        heappush(pq, (grid[nx][ny], nx, ny))
                        v.add((nx, ny))
            ans[t[0]] = anss
        return ans

        