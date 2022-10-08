# 题目：233.数字 1 的个数
# 难度：HARD
# 最后提交：2022-09-15 10:13:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        @cache
        def p(i, c, islimit):
            if i == len(s):
                return c
            res = 0
            up = int(s[i]) if islimit else 9
            for j in range(up+1):
                res += p(i+1,c+(j==1), islimit and j == up)
            return res
        return p(0, 0, True)