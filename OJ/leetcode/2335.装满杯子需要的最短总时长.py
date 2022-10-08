# 题目：2335.装满杯子需要的最短总时长
# 难度：EASY
# 最后提交：2022-07-10 10:33:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        ans = 0
        while amount[0]:
            amount[1] -= 1
            amount[2] -= 1
            ans += 1
            amount.sort()
        ans += amount[1]
        ans += amount[2] - amount[1]
        return ans