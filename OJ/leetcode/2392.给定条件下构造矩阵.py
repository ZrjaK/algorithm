# 题目：2392.给定条件下构造矩阵
# 难度：HARD
# 最后提交：2022-08-28 11:33:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row = defaultdict(list)
        col = defaultdict(list)
        for i, j in rowConditions:
            row[i].append(j)
        for i, j in colConditions:
            col[i].append(j)
        v = set()
        for i in range(1, k+1):
            q = deque([i])
            while q:
                t = q.popleft()
                if t in v:
                    continue
                v.add(t)
                for c in row[t]:
                    if c == i:
                        return []
                    q.append(c)
        v = set()
        for i in range(1, k+1):
            q = deque([i])
            while q:
                t = q.popleft()
                if t in v:
                    continue
                v.add(t)
                for c in col[t]:
                    if c == i:
                        return []
                    q.append(c)
        h = [[i-1, i-1] for i in range(k+1)]
        for _ in range(10):
            for i, j in rowConditions:
                if h[i][0] > h[j][0]:
                    h[j][0], h[i][0] = h[i][0], h[j][0]
            for i, j in colConditions:
                if h[i][1] > h[j][1]:
                    h[j][1], h[i][1] = h[i][1], h[j][1]
        ans = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            ans[h[i][0]][h[i][1]] = i
        return ans
        