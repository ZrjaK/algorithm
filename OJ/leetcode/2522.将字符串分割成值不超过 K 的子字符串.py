# 题目：2522.将字符串分割成值不超过 K 的子字符串
# 难度：MEDIUM
# 最后提交：2023-01-01 10:38:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def p(i):
            if i == n:
                return 0
            res = 1e99
            for j in range(i, n):
                if int(s[i:j+1]) <= k:
                    res = min(res, 1 + p(j+1))
                else:
                    break
            return res
        res = p(0)
        return res if res != 1e99 else -1