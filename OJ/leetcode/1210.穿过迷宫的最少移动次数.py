# 题目：1210.穿过迷宫的最少移动次数
# 难度：HARD
# 最后提交：2022-09-15 11:31:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        from collections import deque
        # 定义状态头坐标+方向：(x,y,0/1)
        row = len(grid)
        col = len(grid[0])
        init = [(0,1,0)]
        # 截止条件
        end = (row-1,col-1,0)
        q = deque(init)
        s = set(init)
        step = 0
        while q:
            for _ in range(len(q)):
                # 6种状态转移方式
                x,y,d = q.popleft()
                if (x,y,d) == end:
                    return step
                # 水平蛇
                if d == 0:
                    if y+1<col and grid[x][y+1] == 0:
                        # 蠕动
                        val = (x, y+1, 0)
                        if val not in s:
                            s.add(val)
                            q.append(val)
                    if x+1 <row and grid[x+1][y] == 0 and grid[x+1][y-1] == 0:
                        # !!头尾一起平移
                        val = (x+1, y, 0)
                        if val not in s:
                            s.add(val)
                            q.append(val)
                        # 旋转
                        val = (x+1, y-1, 1)
                        if val not in s:
                            s.add(val)
                            q.append(val)
                # 垂直蛇
                else:
                    if x+1 <row  and grid[x+1][y] == 0:
                        val = (x+1, y, 1)
                        if val not in s:
                            s.add(val)
                            q.append(val)
                    if y+1<col and grid[x][y+1] == 0 and grid[x-1][y+1] == 0:
                        val = (x, y+1, 1)
                        if val not in s:
                            s.add(val)
                            q.append(val)
                        val = (x-1, y+1, 0)
                        if val not in s:
                            s.add(val)
                            q.append(val)
            step += 1
        # 循环体内未找到，代表抵达不了终点，返回-1
        return -1