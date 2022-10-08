# 题目：901.股票价格跨度
# 难度：MEDIUM
# 最后提交：2022-09-02 21:22:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        res = 0
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res+1])
        return res+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)