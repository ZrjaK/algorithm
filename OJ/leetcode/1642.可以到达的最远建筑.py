# 题目：1642.可以到达的最远建筑
# 难度：MEDIUM
# 最后提交：2022-09-07 11:18:03 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = []
        s = 0
        for i in range(n-1):
            t = heights[i+1] - heights[i]
            if t > 0:
                heappush(pq, t)
                if len(pq) > ladders:
                    s += heappop(pq)
                if s > bricks:
                    return i
        return n - 1