# 题目：2249.统计圆内格点数目
# 难度：MEDIUM
# 最后提交：2022-04-24 10:37:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for x,y,r in circles:
            for i in range(x-r,x+r+1):
                for j in range(y-r,y+r+1):
                    if (i-x)**2+(j-y)**2<=r**2:
                        res.add(tuple([i, j]))
        # print(res)
        return len(res)