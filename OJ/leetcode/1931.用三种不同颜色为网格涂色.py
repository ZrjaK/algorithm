# 题目：1931.用三种不同颜色为网格涂色
# 难度：HARD
# 最后提交：2022-09-21 16:05:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        h = []
        for i in range(3**m):
            c = i
            t = ""
            for j in range(m):
                t += str(c % 3)
                c //= 3
            for j in range(1, m):
                if t[j] == t[j-1]:
                    break
            else:
                h.append(t)
        @cache
        def p(i, pre):
            if i == n:
                return 1
            res = 0
            for f in h:
                for j in range(m):
                    if f[j] == pre[j]:
                        break
                else:
                    res += p(i+1, f)
            return res
        return p(0, "3" * m) % int(1e9+7)