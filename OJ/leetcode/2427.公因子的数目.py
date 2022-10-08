# 题目：2427.公因子的数目
# 难度：EASY
# 最后提交：2022-10-02 10:30:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, b+1):
            if b % i == 0 and a % i == 0:
                ans += 1
        return ans