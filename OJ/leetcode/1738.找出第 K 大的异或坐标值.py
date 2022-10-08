# 题目：1738.找出第 K 大的异或坐标值
# 难度：MEDIUM
# 最后提交：2022-08-26 16:56:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        pq = []
        for i in range(m):
            for j in range(n):
                dp[i][j] = dp[i-1][j] ^ dp[i][j-1] ^ dp[i-1][j-1] ^ matrix[i][j]
                heappush(pq, dp[i][j])
                if len(pq) > k:
                    heappop(pq)
        return heappop(pq)
