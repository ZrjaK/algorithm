# 题目：2338.统计理想数组的数目
# 难度：HARD
# 最后提交：2022-07-10 13:07:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

from math import comb
class Solution:
    def idealArrays(self, n: int, m: int) -> int:
        M = 10 ** 9 + 7
        ans = 1
        for i in range(2, m + 1):
            now = 1
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    cnt = 0
                    while i % j == 0:
                        i //= j
                        cnt += 1
                    now = now * comb(n + cnt - 1, n - 1)
            if i != 1:
                now = now * n
            ans = (ans + now) % M
        return ans