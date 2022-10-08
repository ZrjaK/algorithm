# 题目：1496.判断路径是否相交
# 难度：EASY
# 最后提交：2021-10-19 23:14:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        xy = []
        for i in path:
            xy.append([x, y])
            if i == "E":
                x += 1
            if i == "W":
                x -= 1
            if i == "N":
                y += 1
            if i == "S":
                y -= 1
            if [x, y] in xy:
                return True
        return False