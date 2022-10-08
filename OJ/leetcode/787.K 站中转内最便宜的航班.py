# 题目：787.K 站中转内最便宜的航班
# 难度：MEDIUM
# 最后提交：2022-07-07 14:05:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h = [[1e99] * n for _ in range(n)]
        for i, j, c in flights:
            h[i][j] = c
        @cache
        def p(cur, rest):
            if cur == dst:
                return 0
            if rest < 0:
                return 1e99
            res = 1e99
            for i in range(n):
                if h[cur][i] < 1e9:
                    res = min(res, p(i, rest-1)+h[cur][i])
            return res
        res = p(src, k)
        return res if res < 1e90 else -1