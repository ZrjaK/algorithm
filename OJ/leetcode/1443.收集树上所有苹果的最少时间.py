# 题目：1443.收集树上所有苹果的最少时间
# 难度：MEDIUM
# 最后提交：2022-08-10 17:31:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        v = set()
        def p(i):
            if i in v:
                return [False, 0]
            v.add(i)
            res = 0
            f = False
            if hasApple[i]:
                f = True
            for c in d[i]:
                t = p(c)
                res += t[1]
                f |= t[0]
                if t[0]:
                    res += 2
            return [f, res]
        return p(0)[1]
            