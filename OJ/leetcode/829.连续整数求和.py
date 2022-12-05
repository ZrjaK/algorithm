# 题目：829.连续整数求和
# 难度：HARD
# 最后提交：2022-11-29 20:07:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def check(n, k):
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if check(n, k):
                ans += 1
            k += 1
        return ans