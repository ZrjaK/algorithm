# 题目：1828.统计一个圆中点的数目
# 难度：MEDIUM
# 最后提交：2023-01-24 01:02:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [len([1 for i, j in points if (x-i)**2 + (y-j)**2 <= r**2]) for x, y, r in queries]