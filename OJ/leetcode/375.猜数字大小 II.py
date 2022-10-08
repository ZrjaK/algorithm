# 题目：375.猜数字大小 II
# 难度：MEDIUM
# 最后提交：2022-06-30 18:45:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def p(l, r):
            if l >= r:
                return 0
            res = 1e9
            for i in range(l, r+1):
                res = min(res, i + max(p(l, i-1), p(i+1, r)))
            return res

        return p(1, n)


