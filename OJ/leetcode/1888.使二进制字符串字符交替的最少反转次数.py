# 题目：1888.使二进制字符串字符交替的最少反转次数
# 难度：MEDIUM
# 最后提交：2022-09-08 11:17:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        _s = "10" * (n // 2) + "1" * (n % 2)
        count = 0
        for i in range(n):
            if s[i] == _s[i]:
                count += 1
        if n % 2 == 0:
            return min(count, n-count)
        res = n
        for c in s:
            if c == "1":
                count = n - (count - 1)
            else:
                count = n - (count + 1)
            res = min(res, count, n-count)
        return res