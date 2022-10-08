# 题目：2209.用地毯覆盖后的最少白色砖块
# 难度：HARD
# 最后提交：2022-09-19 14:42:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        @cache
        def p(i, rest):
            if i >= n:
                return 0
            if floor[i] == "0":
                return p(i+1, rest)
            res = 1+p(i+1, rest)
            if rest:
                res = min(res, p(i+carpetLen, rest-1))
            return res
        return p(0, numCarpets)
