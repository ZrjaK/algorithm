# 题目：1987.不同的好子序列数目
# 难度：HARD
# 最后提交：2022-10-16 19:39:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        binary = binary[::-1]
        n = len(binary)
        @cache
        def p(i, c):
            if i == 0:
                return binary[0] == c
            if binary[i] == c:
                return p(i-1, "0") + p(i-1, "1") + 1
            else:
                return p(i-1, c)
        res = p(n-1, "1")
        p.cache_clear()
        if "0" in binary:
            res += 1
        return res % int(1e9+7)
            