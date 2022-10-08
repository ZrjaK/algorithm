# 题目：1575.统计所有可行路径
# 难度：HARD
# 最后提交：2022-09-16 09:46:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        @cache
        def p(i, rest):
            if rest < 0:
                return 0
            res = int(i==finish)
            for j in range(n):
                if i != j:
                    res += p(j, rest-abs(locations[i]-locations[j]))
            return res
        return p(start, fuel) % int(1e9+7)