# 题目：1655.分配重复整数
# 难度：HARD
# 最后提交：2022-09-28 11:30:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        c = list(Counter(nums).values())
        n = len(c)
        m = len(quantity)
        h = [0] * (1<<m)
        for i in range(1<<m):
            h[i] = sum(quantity[k] for k in range(m) if i>>k & 1)
        @cache
        def p(i, state):
            if state+1 == 1<<m:
                return True
            if i == n:
                return False
            if p(i+1, state):
                return True
            f = (1<<m)-1 ^ state
            x = f
            while x:
                t = h[x]
                if c[i] >= t:
                    if p(i+1, state|x):
                        return True
                x = (x-1) & f
            return False
        return p(0, 0)