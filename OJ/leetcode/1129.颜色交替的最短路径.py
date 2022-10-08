# 题目：1129.颜色交替的最短路径
# 难度：MEDIUM
# 最后提交：2022-08-06 02:26:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        r = defaultdict(list)
        for i, j in redEdges:
            r[i].append(j)
        b = defaultdict(list)
        for i, j in blueEdges:
            b[i].append(j)
        co = [r, b]
        res = [[1e99] * 2 for _ in range(n)]
        res[0][0] = 0
        res[0][1] = 0
        pq = [(0, 0, 0), (0, 1, 0)]
        while pq:
            s, c, t = heappop(pq)
            res[t][c] = s
            for nxt in co[c^1][t]:
                if res[t][c] + 1 < res[nxt][c^1]:
                    res[nxt][c^1] = res[t][c] + 1
                    heappush(pq, (s+1, c^1, nxt))
        for i in range(n):
            res[i][0] = min(res[i])
            res[i][1] = min(res[i])
            for j in range(2):
                if res[i][j] > 1e9:
                    res[i][j] = -1
        return [i[0] for i in res]
            