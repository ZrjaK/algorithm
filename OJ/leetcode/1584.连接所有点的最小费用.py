# 题目：1584.连接所有点的最小费用
# 难度：MEDIUM
# 最后提交：2022-08-17 22:03:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = {}
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = parent[find(j)]
        h = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                parent[(points[i][0], points[i][1])] = (points[i][0], points[i][1])
                parent[(points[j][0], points[j][1])] = (points[j][0], points[j][1])
                h.append((i, j, abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])))
        h.sort(key=lambda x:x[2])
        ans = 0
        for i, j, v in h:
            if find((points[i][0], points[i][1])) == find((points[j][0],points[j][1])):
                continue
            union((points[i][0],points[i][1]), (points[j][0],points[j][1]))
            ans += v
        return ans