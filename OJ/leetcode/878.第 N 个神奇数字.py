# 题目：878.第 N 个神奇数字
# 难度：HARD
# 最后提交：2022-11-22 08:47:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l, r = 1, int(1e18)
        while l + 1 < r:
            mid = l + r >> 1
            t = mid // a + mid // b - mid // lcm(a, b)
            if t >= n:
                r = mid
            else:
                l = mid
        return r % int(1e9+7)