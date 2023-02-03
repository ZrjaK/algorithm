# 题目：1701.平均等待时间
# 难度：MEDIUM
# 最后提交：2023-01-16 14:19:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        ans = 0
        cur = 0
        for i, j in customers:
            cur = max(cur, i)
            cur += j
            ans += cur - i
        return ans / n