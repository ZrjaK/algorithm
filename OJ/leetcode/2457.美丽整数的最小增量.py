# 题目：2457.美丽整数的最小增量
# 难度：MEDIUM
# 最后提交：2022-10-30 10:47:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ans = 0
        t = 1
        b = n
        while 1:
            s = str(n)
            if sum([int(i) for i in s]) <= target:
                return ans
            c = n//10**t *10**t + 10**t
            ans = c-b
            n = c
            t += 1
        return ans