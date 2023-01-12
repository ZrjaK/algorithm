# 题目：2513.最小化两个数组中的最大值
# 难度：MEDIUM
# 最后提交：2022-12-25 00:07:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizeSet(self, d1: int, d2: int, c1: int, c2: int) -> int:
        l, r = 0, 10**10
        while l + 1 < r:
            mid = l + r >> 1
            
            m1 = mid - mid // d1
            m2 = mid - mid // d2
            m3 = mid - mid // d1 - mid // d2 + mid // lcm(d1, d2)
            
            m1 -= m3
            m2 -= m3
            
            m3 -= max(0, c1-m1) + max(0, c2-m2)
            if m3 >= 0:
                r = mid
            else:
                l = mid
        return r