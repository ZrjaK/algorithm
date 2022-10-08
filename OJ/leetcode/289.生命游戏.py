# 题目：289.生命游戏
# 难度：MEDIUM
# 最后提交：2022-09-12 12:54:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h01 = []
        h10 = []
        m, n = len(board), len(board[0])
        def calc(i, j):
            s = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0<=x<m and 0<=y<n and (i, j) != (x, y) and board[x][y]:
                        s += 1
            return s
        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    t = calc(i, j)
                    if t != 2 and t != 3:
                        h10.append((i, j))
                else:
                    if calc(i, j) == 3:
                        h01.append((i, j))
        for i, j in h01:
            board[i][j] = 1
        for i, j in h10:
            board[i][j] = 0
