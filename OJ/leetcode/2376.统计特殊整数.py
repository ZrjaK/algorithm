# 题目：2376.统计特殊整数
# 难度：HARD
# 最后提交：2022-09-14 23:39:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

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
