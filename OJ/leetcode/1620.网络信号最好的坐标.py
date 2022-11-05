# 题目：1620.网络信号最好的坐标
# 难度：MEDIUM
# 最后提交：2022-11-02 20:57:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def calc(x1, y1, x2, y2, q):
            d = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if d > radius:
                return 0
            return q // (1 + d) 
        ax = ay = t = 0
        for i in range(51):
            for j in range(51):
                f = 0
                for x, y, q in towers:
                    f += calc(i, j, x, y, q)
                if f > t:
                    ax = i
                    ay = j
                    t = f
                elif t == f:
                    if (i, j) < (ax, ay):
                        ax = i
                        ay = j
        return [ax, ay]