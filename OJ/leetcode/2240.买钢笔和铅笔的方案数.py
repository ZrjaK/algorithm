# 题目：2240.买钢笔和铅笔的方案数
# 难度：MEDIUM
# 最后提交：2022-04-16 22:36:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        for i in range(total//cost1+1):
            ans += (total-i*cost1)//cost2+1
        return ans