# 题目：LCP 63.弹珠游戏
# 难度：MEDIUM
# 最后提交：2022-09-24 18:01:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n, m = len(plate), len(plate[0])
        @cache
        def getRes(posx, posy, d):
            if plate[posx][posy] == 'O': return 0
            if plate[posx][posy] == 'W':
                d = (d-1) % 4
            elif plate[posx][posy] == 'E':
                d = (d+1) % 4
            dx, dy = directions[d]
            if 0 <= posx + dx < n and 0 <= posy + dy < m:
                return getRes(posx + dx, posy + dy, d) + 1
            return inf
        res = []
        for i in range(1, m-1):
            if plate[0][i] == '.' and getRes(0, i, 1) <= num:
                res.append([0, i])
            if plate[n-1][i] == '.' and getRes(n-1, i, 3) <= num:
                res.append([n-1, i])
        for i in range(1, n-1):
            if plate[i][0] == '.' and getRes(i, 0, 0) <= num:
                res.append([i, 0])
            if plate[i][m-1] == '.' and getRes(i, m-1, 2) <= num:
                res.append([i, m-1])
        return res