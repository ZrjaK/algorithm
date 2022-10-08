# 题目：1610.可见点的最大数目
# 难度：HARD
# 最后提交：2022-09-21 13:44:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        h = []
        f = 0
        for x, y in points:
            if x == location[0] and y == location[1]:
                f += 1
                continue
            t = atan2(y-location[1], x-location[0]) * 360 / (2*math.pi)
            h.append(t%360)
        h.sort()
        # print(h)
        h += [i+360 for i in h]
        l = 0
        ans = 0
        for r in range(len(h)):
            while l < len(h) and h[r] - h[l] > angle:
                l += 1
            ans = max(ans, r-l+1)
        return ans + f