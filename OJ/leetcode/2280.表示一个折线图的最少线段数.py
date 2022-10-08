# 题目：2280.表示一个折线图的最少线段数
# 难度：MEDIUM
# 最后提交：2022-05-22 10:59:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x:x[0])
        n = len(stockPrices)
        if n == 1:
            return 0
        ans = 1
        dx = stockPrices[1][0]-stockPrices[0][0]
        dy = stockPrices[1][1]-stockPrices[0][1]
        for i in range(2, n):
            cx = stockPrices[i][0]-stockPrices[i-1][0]
            cy = stockPrices[i][1]-stockPrices[i-1][1]
            if cy * dx != dy * cx:
                ans += 1
            dx = cx
            dy = cy
        return ans