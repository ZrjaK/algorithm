# 题目：786.第 K 个最小的素数分数
# 难度：MEDIUM
# 最后提交：2022-08-28 02:03:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                heappush(pq, [-arr[i]/arr[j], arr[i], arr[j]])
                if len(pq) > k:
                    heappop(pq)
        return pq[0][1:]