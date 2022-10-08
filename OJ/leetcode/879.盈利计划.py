# 题目：879.盈利计划
# 难度：HARD
# 最后提交：2022-09-23 23:19:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        @cache
        def p(i, rest, prof):
            if rest < 0:
                return 0
            if i == m:
                return 1 if prof >= minProfit else 0
            res = p(i+1, rest, prof) + p(i+1, rest-group[i], min(prof+profit[i], minProfit))
            return res
        res = p(0, n, 0) % int(1e9+7)
        p.cache_clear()
        return res
            
            
            