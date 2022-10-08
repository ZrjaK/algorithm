# 题目：1573.分割字符串的方案数
# 难度：MEDIUM
# 最后提交：2022-05-08 20:46:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numWays(self, s: str) -> int:
        t = s.count("1")
        if t % 3 != 0:
            return 0
        n = len(s)
        if t == 0:
            return (n-1)*(n-2)//2 % int(1e9+7)
        l = r = c = 0
        t //= 3
        ans = 1
        for i in range(n):
            if s[i] == "1":
                c += 1
            if c == t:
                l = i
                break
        for i in range(l+1, n):
            if s[i] == "1":
                c += 1
            if c == t + 1:
                ans *= i-l
                break
        c = 0
        for i in range(n):
            if s[i] == "1":
                c += 1
            if c == t*2:
                r = i
                break
        for i in range(r+1, n):
            if s[i] == "1":
                c += 1
            if c == t*2+1:
                ans *= i-r
                break
        return ans % int(1e9+7)
            