# 题目：939.最小面积矩形
# 难度：MEDIUM
# 最后提交：2022-08-29 19:46:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = 1e99

        for x in sorted(columns):
            column = sorted(columns[x])
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < 1e90 else 0