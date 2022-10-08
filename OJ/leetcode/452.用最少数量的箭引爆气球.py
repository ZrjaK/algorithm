# 题目：452.用最少数量的箭引爆气球
# 难度：MEDIUM
# 最后提交：2022-08-27 23:41:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        t = points[0][1]
        ans = 1
        for l, r in points:
            if l > t:
                ans += 1
                t = r
        return ans