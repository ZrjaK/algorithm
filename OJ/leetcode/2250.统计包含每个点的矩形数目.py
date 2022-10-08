# 题目：2250.统计包含每个点的矩形数目
# 难度：MEDIUM
# 最后提交：2022-04-24 11:13:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        d = {}
        for x,y in rectangles:
            if y in d:
                d[y].append(x)
            else:
                d[y] = [x]
        # print(d)
        for i in d.keys():
            d[i].sort()
        rectangles.sort(key=lambda x:x[1])
        ry = [i[1] for i in rectangles]
        res = []
        for x, y in points:
            a = 0
            for i in range(y, 101):
                if i in d:
                    a += len(d[i])-bisect_left(d[i], x)
            res.append(a)
        return res