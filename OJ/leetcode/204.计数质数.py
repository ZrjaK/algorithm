# 题目：204.计数质数
# 难度：MEDIUM
# 最后提交：2022-08-24 15:43:14 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPrimes(self, n: int) -> int:
        l = [1] * n
        p = []
        for i in range(2, n):
            if l[i]:
                p.append(i)
            j = 0
            for j in p:
                if i * j >= n:
                    break
                l[i*j] = 0
                if i % j == 0:
                    break
        return len(p)