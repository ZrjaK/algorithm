# 题目：1052.爱生气的书店老板
# 难度：MEDIUM
# 最后提交：2022-05-22 22:59:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = 0
        for i, j in zip(customers, grumpy):
            if not j:
                s += i
        l = r = 0
        while r < minutes:
            if grumpy[r]:
                s += customers[r]
            r += 1
        ans = s
        while r < len(customers):
            if grumpy[r]:
                s += customers[r]
            if grumpy[l]:
                s -= customers[l]
            r += 1
            l += 1
            ans = max(ans, s)
        return ans