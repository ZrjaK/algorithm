# 题目：2578.最小和分割
# 难度：EASY
# 最后提交：2023-03-04 22:31:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def splitNum(self, num: int) -> int:
        h = []
        while num:
            h.append(num % 10)
            num //= 10
        h.sort()
        s1 = s2 = 0
        for i in h[::2]:
            s1 = s1 * 10 + i
        for i in h[1::2]:
            s2 = s2 * 10 + i
        return s1 + s2