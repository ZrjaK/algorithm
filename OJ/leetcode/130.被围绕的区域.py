# 题目：130.被围绕的区域
# 难度：MEDIUM
# 最后提交：2022-07-26 01:55:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if (i, j) in visited or board[i][j] == "X":
                    continue
                t = []
                o = True
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    if (x, y) in visited:
                        continue
                    t.append([x, y])
                    visited.add((x, y))
                    if x > 0 and board[x-1][y] == "O":
                        q.append([x-1, y])
                    if x < m-1 and board[x+1][y] == "O":
                        q.append([x+1, y])
                    if y > 0 and board[x][y-1] == "O":
                        q.append([x, y-1])
                    if y < n-1 and board[x][y+1] == "O":
                        q.append([x, y+1])
                for x, y in t:
                    if x == m-1 or x == 0 or y == n-1 or y == 0:
                        o = False
                if o:
                    for x, y in t:
                        board[x][y] = "X"
                    