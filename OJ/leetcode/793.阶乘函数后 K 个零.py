# 题目：793.阶乘函数后 K 个零
# 难度：HARD
# 最后提交：2022-09-19 13:17:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def p(x):
            ans = 0
            while x:
                x //= 5
                ans += x
            return ans
        l, r = 0, 10**10
        while l <= r:
            mid = l+r>>1
            if p(mid) < k:
                l = mid + 1
            else:
                r = mid - 1
        return 5 if p(l) == k else 0