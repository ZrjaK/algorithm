# 题目：1716.计算力扣银行的钱
# 难度：EASY
# 最后提交：2022-04-12 02:13:34 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            ans += (i-1)//7 + (i-1)%7 + 1
        return ans