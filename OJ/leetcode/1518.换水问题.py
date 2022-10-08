# 题目：1518.换水问题
# 难度：EASY
# 最后提交：2021-10-19 23:47:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remaining = numBottles
        empty = 0
        drinked = 0
        exchange = 0
        while remaining != 0:
            drinked += remaining
            empty += remaining
            remaining = empty // numExchange
            empty = empty % numExchange
        return drinked