# 题目：面试题 17.09.第 k 个数
# 难度：MEDIUM
# 最后提交：2022-09-28 09:41:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        factors = [3, 5, 7]
        seen = {1}
        heap = [1]

        for i in range(k - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)