# 题目：753.破解保险箱
# 难度：HARD
# 最后提交：2022-09-27 09:05:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        v = set()
        ans = t = "0" * n
        v.add(t)
        while len(v) < k**n:
            f = t[1:]
            for j in range(k-1, -1, -1):
                c = f + str(j)
                if c not in v:
                    v.add(c)
                    ans += str(j)
                    t = c
                    break
        return ans