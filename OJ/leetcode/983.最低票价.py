# 题目：983.最低票价
# 难度：MEDIUM
# 最后提交：2022-07-12 01:35:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        s = set(days)
        @cache
        def p(day):
            if day > days[-1]:
                return 0
            if day not in s:
                return p(day+1)
            return min(p(day+1)+costs[0], p(day+7)+costs[1], p(day+30)+costs[2])
            
        return p(0)
            