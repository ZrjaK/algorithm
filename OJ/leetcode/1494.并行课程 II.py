# 题目：1494.并行课程 II
# 难度：HARD
# 最后提交：2022-09-18 20:45:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        @cache
        def dfs(state):
            if state == (1 << n) - 1:
                return 0
            nex = [i for i in range(n) if not state & (1 << i) and state & pre[i] == pre[i]]
            res = n + 1
            for sub in combinations(nex, min(k, len(nex))):
                res = min(res, 1 + dfs(state | sum([1 << i for i in sub])))
            return res

        pre = [0] * n
        for i, j in relations:
            pre[j - 1] |= 1 << (i - 1)
        return dfs(0)