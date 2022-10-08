# 题目：2257.统计网格图中没有被保卫的格子数
# 难度：MEDIUM
# 最后提交：2022-05-01 09:50:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        f = [[0] * n for _ in range(m)]
        for x,y in walls :
            f[x][y] = -1
        for x,y in guards :
            f[x][y] = -2
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for x,y in guards :
            for dx, dy in d :
                nx, ny = x, y
                while True :
                    nx += dx
                    ny += dy
                    if 0 <= nx < m and 0 <= ny < n :
                        if f[nx][ny] < 0 :
                            break
                        if f[nx][ny] == 0 :
                            f[nx][ny] = 1
                    else :
                        break
        res = 0
        for i in range(m) :
            for j in range(n) :
                if f[i][j] == 0 :
                    res += 1
        return res