# 题目：2045.到达目的地的第二短时间
# 难度：HARD
# 最后提交：2022-09-23 17:00:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        v = set()
        dist1 = [1e99] * (n+1)
        dist2 = [1e99] * (n+1)
        dist1[1] = 0
        pq = [[0, 1]]
        while pq:
            s, t = heappop(pq)
            if (s, t) in v:
                continue
            v.add((s, t))
            if (s // change) % 2:
                s = change * (s // change + 1)
            for j in d[t]:
                if s + time < dist1[j]:
                    dist1[j] = s + time
                    heappush(pq, [dist1[j], j])
                elif s + time > dist1[j]:
                    dist2[j] = min(dist2[j], s + time)
                    heappush(pq, [dist2[j], j])
        return dist2[n]