# 题目：691.贴纸拼词
# 难度：HARD
# 最后提交：2022-08-25 22:47:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        @cache
        def p(m):
            if m == 0:
                return 0
            res = 1e99
            for s in stickers:
                c = Counter(s)
                t = m
                for i, v in enumerate(target):
                    if 1<<i & m and c[v]:
                        c[v] -= 1
                        t ^= 1<<i
                if t != m:
                    res = min(res, 1 + p(t))
            return res
        res = p((1<<n)-1)
        p.cache_clear()
        return res if res < 1e9 else -1