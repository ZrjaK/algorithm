# 题目：1994.好子集的数目
# 难度：HARD
# 最后提交：2022-10-18 10:17:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

h = [[] for _ in range(31)]
f = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for i in range(2, 31):
    c = i
    for j in f:
        while c % j == 0:
            c //= j
            h[i].append(j)
    if len(set(h[i])) != len(h[i]):
        h[i] = []
d = {v: i for i, v in enumerate(f)}

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        @cache
        def p(i, mask):
            if i == 31:
                return int(mask != 0)
            if not cnt[i] or not h[i] or any(mask>>d[prime] & 1 == 1 for prime in h[i]):
                return p(i+1, mask)
            return p(i+1, mask) + cnt[i] * p(i+1, mask|sum(1<<d[prime] for prime in h[i]))
        res = (1<<cnt[1]) * p(2, 0) % int(1e9+7)
        p.cache_clear()
        return res