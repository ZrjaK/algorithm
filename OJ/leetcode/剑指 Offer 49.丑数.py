# 题目：剑指 Offer 49.丑数
# 难度：MEDIUM
# 最后提交：2022-10-03 18:49:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        v = {1}
        pq = [1]

        for i in range(n - 1):
            t = heappop(pq)
            for f in factors:
                if (nxt := t * f) not in v:
                    v.add(nxt)
                    heappush(pq, nxt)

        return pq[0]