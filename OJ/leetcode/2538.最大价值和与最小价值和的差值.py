# 题目：2538.最大价值和与最小价值和的差值
# 难度：HARD
# 最后提交：2023-01-15 11:41:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        ind = [0] * n
        d = defaultdict(list)
        for i, j in edges:
            ind[i] += 1
            ind[j] += 1
            d[i].append(j)
            d[j].append(i)
        @cache
        def dfs(i, fa):
            if len(d[i]) == 1 and fa != -1:
                return [0, price[i]]
            res = [0, 0]
            for j in d[i]:
                if j != fa:
                    r = dfs(j, i)
                    if r[0] > res[0]:
                        res[0] = r[0]
                        res[1] = r[1]
            res[0] += price[i]
            return res
        ans = 0
        for i in range(n):
            if ind[i] == 1:
                r = dfs(i, -1)
                ans = max(ans, r[0] + r[1] - min(price[i], r[1]))
        return ans