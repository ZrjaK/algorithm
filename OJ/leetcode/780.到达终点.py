# 题目：780.到达终点
# 难度：HARD
# 最后提交：2022-04-09 00:20:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        @lru_cache(None)
        def p(x, y):
            if x < sx or y < sy:
                return False
            if x == sx:
                return (y-sy)%x == 0
            if y == sy:
                return (x-sx)%y == 0
            if x > y:
                return p(x%y,y)
            else:
                return p(x,y%x)
        return p(tx,ty)