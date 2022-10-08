# 题目：LCP 66.最小展台数量
# 难度：EASY
# 最后提交：2022-10-07 15:03:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        c = [0] * 26
        for i in range(26):
            for s in demand:
                t = 0
                for j in s:
                    if ord(j)-97 == i:
                        t += 1
                c[i] = max(c[i], t)
        return sum(c)