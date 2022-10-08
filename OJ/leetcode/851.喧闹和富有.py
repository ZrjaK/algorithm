# 题目：851.喧闹和富有
# 难度：MEDIUM
# 最后提交：2022-05-22 01:17:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        d = defaultdict(list)
        for i, j in richer:
            d[j].append(i)
        res = [-1] * n
        def dfs(p):
            if res[p] >= 0:
                return res[p]
            res[p] = p
            for i in d[p]:
                if quiet[res[p]] > quiet[dfs(i)]:
                    res[p] = res[i]
            return res[p]
        
        for p in range(n):
            dfs(p)
        return res