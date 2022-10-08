# 题目：1453.圆形靶内的最大飞镖数量
# 难度：HARD
# 最后提交：2022-09-23 17:38:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def calc(p0, p1):
            if p1[0] == p0[0]:
                y0 = y1 = (p0[1]+p1[1]) / 2
                deltay = (y0-p0[1]) ** 2
                deltax = sqrt(r ** 2 - deltay)
                x0 = p1[0] - deltax
                x1 = p1[0] + deltax
            else:
                C1 = (p1[0]**2 + p1[1]**2 - p0[0]**2 - p0[1]**2) / 2 / (p1[0] - p0[0])
                C2 = (p1[1] - p0[1]) / (p1[0] - p0[0])
                A = 1 + C2**2
                B = 2 * (p0[0] - C1) * C2 - 2*p0[1]
                C = (p0[0]-C1)**2 + p0[1]**2 - r**2
                y0 = (-B + sqrt(B*B - 4 * A * C)) / 2 / A
                y1 = (-B - sqrt(B*B - 4 * A * C)) / 2 / A
                x0 = C1 - C2 * y0
                x1 = C1 - C2 * y1
            return [[x0, y0], [x1, y1]]
        ans = 1
        n = len(darts)
        for i in range(n):
            for j in range(i+1, n):
                if (darts[i][0]-darts[j][0])**2 + (darts[i][1]-darts[j][1])**2 > 4*r**2:
                    continue
                for x, y in calc(darts[i], darts[j]):
                    s = 0
                    for a, b in darts:
                        if (a-x)**2 + (b-y)**2 <= r**2:
                            s += 1
                    ans = max(ans, s)
        return ans