# 题目：973.最接近原点的 K 个点
# 难度：MEDIUM
# 最后提交：2022-08-30 02:04:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i, j in points:
            heappush(pq, [-(i**2+j**2), i, j])
            if len(pq) > k:
                heappop(pq)
        return [i[1:] for i in pq]