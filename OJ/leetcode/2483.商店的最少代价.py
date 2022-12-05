# 题目：2483.商店的最少代价
# 难度：MEDIUM
# 最后提交：2022-11-27 01:52:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans = customers.count("N")
        ansn = n
        c = ans
        for j in range(n-1, -1, -1):
            if customers[j] == "Y":
                c += 1
            else:
                c -= 1
            if c <= ans:
                ansn = j
                ans = c
        return ansn
        