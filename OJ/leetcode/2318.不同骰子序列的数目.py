# 题目：2318.不同骰子序列的数目
# 难度：HARD
# 最后提交：2022-09-19 10:28:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distinctSequences(self, n: int) -> int:
        @cache
        def p(i, pre):
            if i == 0:
                return 1
            res = 0
            for x in range(1, 7):
                if x != pre[0] and x != pre[1] and gcd(x, pre[1]) == 1:
                    res += p(i-1, (pre[1], x))
            return res
        return p(n, (7, 7)) % int(1e9+7)