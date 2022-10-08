# 题目：1125.最小的必要团队
# 难度：HARD
# 最后提交：2022-09-26 22:57:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        d = {}
        n = len(req_skills)
        for i in range(n):
            d[req_skills[i]] = i
        h = []
        for i in people:
            t = 0
            for j in i:
                t |= 1<<d[j]
            h.append(t)
        
        @cache
        def p(i, state):
            if state+1 == 1<<n:
                return []
            if i == len(h):
                return [0] * 30
            res1 = p(i+1, state|h[i]) + [i]
            res2 = p(i+1, state)
            if len(res1) < len(res2):
                return res1
            else:
                return res2
        return p(0, 0)