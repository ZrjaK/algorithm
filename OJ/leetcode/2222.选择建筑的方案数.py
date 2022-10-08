# 题目：2222.选择建筑的方案数
# 难度：MEDIUM
# 最后提交：2022-04-03 13:25:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfWays(self, s: str) -> int:
        def p(g):
            a = b = c = 0
            for i in s:
                if i == g[0]:
                    a += 1
                if i == g[1]:
                    b += a
                if i == g[2]:
                    c += b
            return c
        
        return p("101") + p("010")