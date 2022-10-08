# 题目：1444.切披萨的方案数
# 难度：HARD
# 最后提交：2022-09-20 16:35:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        h = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                h[i][j] = h[i-1][j] + h[i][j-1] - h[i-1][j-1]
                if pizza[i][j] == "A":
                    h[i][j] += 1
        @cache
        def p(i, j, rest):
            if rest == 0:
                if h[m-1][n-1] - h[i-1][n-1] - h[m-1][j-1] + h[i-1][j-1] > 0:
                    return 1
                else:
                    return 0
            res = 0
            for x in range(i, m):
                if h[x-1][n-1] - h[i-1][n-1] - h[x-1][j-1] + h[i-1][j-1] > 0:
                    res += p(x, j, rest-1)
            for y in range(j, n):
                if h[m-1][y-1] - h[m-1][j-1] - h[i-1][y-1] + h[i-1][j-1] > 0:
                    res += p(i, y, rest-1)
            return res
        return p(0, 0, k-1) % int(1e9+7)