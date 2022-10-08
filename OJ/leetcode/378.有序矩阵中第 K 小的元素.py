# 题目：378.有序矩阵中第 K 小的元素
# 难度：MEDIUM
# 最后提交：2022-04-30 21:27:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(pq)[0]