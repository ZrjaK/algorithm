# 题目：2305.公平分发饼干
# 难度：MEDIUM
# 最后提交：2022-06-12 11:22:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        @cache
        def p(h, j, l):
            if j == 1:
                return l+sum([cookies[i] for i in range(len(cookies)) if h[i] == 0])
            res = 1e99
            s = l
            h = list(h)
            for i in range(len(cookies)):
                res = min(res, max(p(tuple(h), j-1, 0), s))
                if h[i] != 1:
                    h[i] = 1
                    s += cookies[i]
                    res = min(res, max(p(tuple(h), j, s), s))
                    h[i] = 0
                    s -= cookies[i]
            return res
        
        return p(tuple([0] * len(cookies)), k, 0)