# 题目：2050.并行课程 III
# 难度：HARD
# 最后提交：2022-09-19 08:10:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        d = defaultdict(list)
        for i, j in relations:
            d[j].append(i)
        @cache
        def p(i):
            res = 0
            for j in d[i]:
                res = max(res, p(j))
            return res + time[i-1]
        res = 0
        for i in range(1, n+1):
            res = max(res, p(i))
        return res