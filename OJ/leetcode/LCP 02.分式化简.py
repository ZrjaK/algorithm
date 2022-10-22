# 题目：LCP 02.分式化简
# 难度：EASY
# 最后提交：2022-10-20 14:54:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        f = [1, cont.pop()]
        while cont:
            t = cont.pop()
            f[0] += t * f[1]
            f = f[::-1]
        t = gcd(f[0], f[1])
        return [f[1]//t, f[0]//t]