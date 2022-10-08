# 题目：2412.完成所有交易的初始最少钱数
# 难度：HARD
# 最后提交：2022-09-17 23:38:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        h = []
        l = []
        for cost, back in transactions:
            if back >= cost:
                l.append([cost, back])
            else:
                h.append([cost, back])
        print(h)
        s = sum([i[0]-i[1] for i in h] + [0])
        f = max([i[1] for i in h] + [0])
        c = max([i[0] for i in l] + [0])
        return s + max(f, c)