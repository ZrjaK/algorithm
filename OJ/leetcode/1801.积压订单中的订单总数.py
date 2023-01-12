# 题目：1801.积压订单中的订单总数
# 难度：MEDIUM
# 最后提交：2023-01-02 00:58:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        from sortedcontainers import SortedList
        buy = SortedList()
        sell = SortedList()
        for price, amount, typ in orders:
            if typ == 1:
                while buy and buy[-1][0] >= price and amount:
                    t = list(buy.pop())
                    newamount = max(0, amount - t[1])
                    t[1] -= amount - newamount
                    if t[1]:
                        buy.add(tuple(t))
                    amount = newamount
                if amount:
                    sell.add((price, amount))
            else:
                while sell and sell[0][0] <= price and amount:
                    t = list(sell.pop(0))
                    newamount = max(0, amount - t[1])
                    t[1] -= amount - newamount
                    if t[1]:
                        sell.add(tuple(t))
                    amount = newamount
                if amount:
                    buy.add((price, amount))
        return (sum(i[1] for i in buy) + sum(i[1] for i in sell)) % int(1e9+7)