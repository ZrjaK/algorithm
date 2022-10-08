# 题目：935.骑士拨号器
# 难度：MEDIUM
# 最后提交：2022-07-09 01:37:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        n1379, n46, n28, n0 = 4,2,2,1
        for _ in range(n - 1):
            n1379, n46, n28, n0 = (n46+n28)*2, n1379+n0*2, n1379, n46
        return(sum([n1379, n46, n28, n0]) % (10**9 + 7))