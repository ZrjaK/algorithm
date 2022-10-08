# 题目：1201.丑数 III
# 难度：MEDIUM
# 最后提交：2022-09-16 08:12:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = math.lcm(a, b)
        ac = math.lcm(a, c)
        bc = math.lcm(c, b)
        abc = math.lcm(a, b, c)
        def check(num):
            cnt = 0
            cnt += num // a
            cnt += num // b
            cnt += num // c
            cnt -= num // ab
            cnt -= num // ac
            cnt -= num // bc
            cnt += num // abc
            return cnt >= n
        l = 1
        r = 2*10**9
        while l <= r:
            mid = l+r>>1
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l if check(l) else r