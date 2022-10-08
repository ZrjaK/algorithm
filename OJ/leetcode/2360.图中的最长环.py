# 题目：2360.图中的最长环
# 难度：HARD
# 最后提交：2022-07-31 11:51:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        v = set()
        for i in range(n):
            if i in v:
                continue
            t = i
            c = 0
            d = {t: 0}
            while edges[t] != -1:
                e = edges[t]
                v.add(t)
                if e in d:
                    ans = max(ans, c-d[e]+1)
                    break
                c += 1
                d[e] = c
                t = e
                if e in v:
                    break
        return ans