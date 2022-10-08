# 题目：面试题 17.06.2出现的次数
# 难度：HARD
# 最后提交：2022-09-15 10:14:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)
        @cache
        def p(i, c, islimit):
            if i == len(s):
                return c
            res = 0
            up = int(s[i]) if islimit else 9
            for j in range(up+1):
                res += p(i+1,c+(j==2), islimit and j == up)
            return res
        return p(0, 0, True)