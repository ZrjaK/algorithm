# 题目：2467.树上最大得分和路径
# 难度：MEDIUM
# 最后提交：2022-11-13 13:58:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        d = defaultdict(list)
        g = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        h = []
        def p(i, fa):
            if i == 0:
                h.append(0)
                return True
            for j in d[i]:
                if j == fa:
                    continue
                res = p(j, i)
                if res:
                    h.append(i)
                    return True
            return False
        p(bob, -1)
        h = h[::-1]
        h = {v: i for i, v in enumerate(h)}
        @cache
        def dfs(i, t, fa):
            res = -1e99
            for nxt in d[i]:
                if nxt == fa:
                    continue
                res = max(res, dfs(nxt, t+1, i))
            if res == -1e99:
                res = 0
            if i in h:
                if t < h[i]:
                    res += amount[i]
                elif t == h[i]:
                    res += amount[i] // 2
            else:
                res += amount[i]
            return res
        return dfs(0, 0, -1)