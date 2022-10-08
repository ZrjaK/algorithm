# 题目：738.单调递增的数字
# 难度：MEDIUM
# 最后提交：2022-09-05 11:33:37 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(int(i) for i in str(n))
        l = len(s)
        t = l
        for i in range(l-1, 0, -1):
            if s[i-1] > s[i]:
                t = i
                s[i-1] -= 1
        while t < l:
            s[t] = 9
            t += 1
        return int("".join([str(i) for i in s]))