# 题目：1184.公交站间的距离
# 难度：EASY
# 最后提交：2021-11-13 21:28:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        m = max(sum(distance[start:destination]), sum(distance[destination:start]))
        return min(m, sum(distance) - m)