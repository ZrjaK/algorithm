from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def p(i, mask, islimit, isnum):
            if i == len(s):
                return int(isnum)
            res = 0
            if not isnum:
                res = p(i+1, mask, False, False)
            up = int(s[i]) if islimit else 9
            for j in range(1-int(isnum), up+1):
                if mask>>j & 1:
                    continue
                res += p(i+1, mask|1<<j, islimit and j == up, True)
            return res
        return p(0, 0, True, False)


# https://leetcode.cn/problems/count-special-integers/

# 2376. 统计特殊整数

# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。

# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。

