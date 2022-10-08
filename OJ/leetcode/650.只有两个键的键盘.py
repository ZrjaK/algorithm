# 题目：650.只有两个键的键盘
# 难度：MEDIUM
# 最后提交：2022-07-06 13:22:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def p(cur, copy):
            if len(cur) == n:
                return 0
            if len(cur) > n:
                return 1e99
            return min(2 + p(cur+cur, cur), 1 + p(cur+copy, copy))
        if n == 1:
            return 0
        return 1 + p("A", "A")