# 题目：2466.统计构造好字符串的方案数
# 难度：MEDIUM
# 最后提交：2022-11-13 13:23:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def p(i):
            if i > high:
                return 0
            return (int(i>=low) + p(i+zero) + p(i+one)) % int(1e9+7)
        return p(0) % int(1e9+7)
