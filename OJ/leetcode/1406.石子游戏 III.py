# 题目：1406.石子游戏 III
# 难度：HARD
# 最后提交：2022-09-15 21:18:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        h = list(accumulate(stoneValue)) + [0]
        @cache
        def p(i):
            if i == n:
                return 0
            res = h[i]-h[i-1]-p(i+1)
            if i+2 <= n:
                res = max(res, h[i+1]-h[i-1]-p(i+2))
            if i+3 <= n:
                res = max(res, h[i+2]-h[i-1]-p(i+3))
            return res
        res = p(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"