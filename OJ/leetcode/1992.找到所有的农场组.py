# 题目：1992.找到所有的农场组
# 难度：MEDIUM
# 最后提交：2022-08-12 12:27:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    t = []
                    q = deque([[i, j]])
                    land[i][j] = 0
                    while q:
                        x, y = q.popleft()
                        t.append([x, y])
                        for dx, dy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                            if 0<=dx<m and 0<=dy<n and land[dx][dy]:
                                land[dx][dy] = 0
                                q.append([dx, dy])
                    t.sort(key=lambda x:x[1])
                    t.sort(key=lambda x:x[0])
                    res.append([t[0][0], t[0][1], t[-1][0], t[-1][1]])
        return  res