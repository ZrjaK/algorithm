# 题目：1878.矩阵中最大的三个菱形和
# 难度：MEDIUM
# 最后提交：2022-09-01 02:13:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # 枚举法，找到所有菱形的情况，再进行排序
        m, n = len(grid), len(grid[0])
        res = set()
        # 枚举所有的菱形
        for i in range(m):
            for j in range(n):
                # 添加面积为0的菱形
                res.add(grid[i][j])
                # 以当前点为中心，菱形的最大范围，上下左右的最小距离
                length = min(i, j, m-1-i, n-1-j)
                for l in range(1, length+1):
                    cur = 0
                    # 先加四个角
                    cur += grid[i-l][j]
                    cur += grid[i+l][j]
                    cur += grid[i][j-l]
                    cur += grid[i][j+l]
                    # 再加上其它边上的元素
                    for k in range(1, l):
                        cur += grid[i-k][j-l+k]
                        cur += grid[i+k][j-l+k]
                        cur += grid[i-k][j+l-k]
                        cur += grid[i+k][j+l-k]
                    # 加上当前矩形
                    res.add(cur)
        
        # 排序以后返回最大的三个
        res = list(res)
        res.sort(reverse=True)
        return res[:3]