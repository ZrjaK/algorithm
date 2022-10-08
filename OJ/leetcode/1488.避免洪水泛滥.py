# 题目：1488.避免洪水泛滥
# 难度：MEDIUM
# 最后提交：2022-09-07 09:25:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        c = []
        d = {}
        for i, v in enumerate(rains):
            if not v:
                c.append(i)
                continue
            ans[i] = -1
            if v in d:
                t = bisect_left(c, d[v])
                if t >= len(c):
                    return []
                ans[c[t]] = v
                c = c[:t] + c[t+1:]
            d[v] = i
        return ans