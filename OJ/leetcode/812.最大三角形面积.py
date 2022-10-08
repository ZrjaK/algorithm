# 题目：812.最大三角形面积
# 难度：EASY
# 最后提交：2021-10-24 13:29:39 +0800 CST
# 语言：python3
# 作者：ZrjaK

import numpy as np
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxarea = 0
        A = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    A = [points[i]+[1], points[j]+[1], points[k]+[1]]
                    A = np.mat(A)
                    maxarea = max(maxarea, abs(np.linalg.det(A)) / 2)
        return maxarea