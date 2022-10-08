# 题目：1434.每个人戴不同帽子的方案数
# 难度：HARD
# 最后提交：2022-09-27 08:52:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        h = [0] * 41
        n = len(hats)
        for i in range(1, 41):
            for j in range(n):
                for k in hats[j]:
                    if k == i:
                        h[i] |= 1<<j
        @cache
        def p(i, state):
            if state+1 == 1<<n:
                return 1
            if i == 41:
                return 0
            res = p(i+1, state)
            for j in range(n):
                if not state>>j & 1 and h[i]>>j & 1:
                    res += p(i+1, state|1<<j)
            return res
        return p(0, 0) % int(1e9+7)