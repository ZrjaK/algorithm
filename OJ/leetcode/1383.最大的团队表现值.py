# 题目：1383.最大的团队表现值
# 难度：HARD
# 最后提交：2022-09-19 10:57:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        l = sorted(zip(speed, efficiency), key=lambda x: x[1])
        ans = 0
        pq = []
        s = 0
        while l:
            f = l.pop()
            heappush(pq, f[0])
            s += f[0]
            if len(pq) > k:
                s -= heappop(pq)
            ans = max(ans, f[1] * s)
        return ans % int(1e9+7)