# 题目：1792.最大平均通过率
# 难度：MEDIUM
# 最后提交：2023-02-19 00:00:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for i, j in classes:
            heappush(pq, [-((i+1)/(j+1)-i/j), i, j])
        while extraStudents:
            _, i, j = heappop(pq)
            i += 1
            j += 1
            extraStudents -= 1
            heappush(pq, [-((i+1)/(j+1)-i/j), i, j])
        return sum(i/j for _, i, j in pq) / len(pq)