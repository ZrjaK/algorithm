# 题目：2073.买票需要的时间
# 难度：EASY
# 最后提交：2023-01-03 01:27:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while tickets[k]:
            for i in range(len(tickets)):
                if not tickets[i]:
                    continue
                tickets[i] -= 1
                ans += 1
                if i == k and not tickets[i]:
                    break
        return ans