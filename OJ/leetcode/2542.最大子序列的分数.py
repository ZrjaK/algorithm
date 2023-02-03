# 题目：2542.最大子序列的分数
# 难度：MEDIUM
# 最后提交：2023-01-22 00:41:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        h = [[i, j] for i, j in zip(nums1, nums2)]
        h.sort(key=lambda x: x[1], reverse=True)
        pq = []
        s = 0
        for i in range(k-1):
            heappush(pq, h[i][0])
            s += h[i][0]
        ans = 0
        for i in range(k-1, n):
            s += h[i][0]
            ans = max(ans, s * h[i][1])
            heappush(pq, h[i][0])
            s -= heappop(pq)
        return ans
        