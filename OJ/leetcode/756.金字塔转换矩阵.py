# 题目：756.金字塔转换矩阵
# 难度：MEDIUM
# 最后提交：2022-08-01 16:33:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = defaultdict(list)
        for allow in allowed:
            d[allow[:2]].append(allow[2])
        @cache
        def p(s):
            t = []
            for i in range(1, len(s)):
                chs = d[s[i - 1] + s[i]]
                if len(chs) == 0: return False
                t.append(chs)
            if len(t) == 1: return True
            for chs in product(*t):
                if p("".join(chs)):
                    return True
            return False
        res = p(bottom)
        p.cache_clear()
        return res