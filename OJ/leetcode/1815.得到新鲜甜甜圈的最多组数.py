# 题目：1815.得到新鲜甜甜圈的最多组数
# 难度：HARD
# 最后提交：2022-09-06 09:42:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        groups = [i % batchSize for i in groups]
        res = groups.count(0)
        groups = [i for i in groups if i]
        n = len(groups)
        @cache
        def p(state, mod):
            if not state:
                return 0
            res = 0
            v = set()
            for i in range(n):
                if 1<<i & state and groups[i] not in v:
                    v.add(groups[i])
                    res = max(res, p(state^1<<i, (mod+groups[i]) % batchSize))
            return res + 1 if not mod else res
        return p((1<<n)-1, 0) + res